"""Check the static GitHub Pages site without network requests or dependencies."""
from html.parser import HTMLParser
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "docs"


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.anchors: list[str] = []
        self.stylesheets: list[str] = []
        self.assets: list[str] = []
        self.titles = 0
        self.h1s = 0
        self.external_scripts = 0
        self.images_without_alt = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            if attrs["id"] in self.ids:
                raise ValueError("Duplicate HTML ID: " + attrs["id"])
            self.ids.add(attrs["id"])
        if tag == "a" and "href" in attrs:
            self.anchors.append(attrs["href"])
        if tag == "link":
            if attrs.get("rel") == "stylesheet":
                self.stylesheets.append(attrs.get("href", ""))
            if attrs.get("rel") == "icon":
                self.assets.append(attrs.get("href", ""))
        if tag == "h1":
            self.h1s += 1
        if tag == "title":
            self.titles += 1
        if tag == "script" and attrs.get("src"):
            self.external_scripts += 1
        if tag == "img" and "alt" not in attrs:
            self.images_without_alt += 1


def main():
    page = SITE / "index.html"
    if not page.is_file():
        raise ValueError("docs/index.html does not exist")
    parser = SiteParser()
    parser.feed(page.read_text(encoding="utf-8"))
    if parser.h1s != 1 or parser.titles != 1:
        raise ValueError("Expected one page title and one H1")
    if parser.external_scripts or parser.images_without_alt:
        raise ValueError("External scripts or images missing alt attributes")
    required = {"main", "top", "research", "engineering", "publications", "education", "credentials", "leadership"}
    if not required.issubset(parser.ids):
        raise ValueError("Missing navigation landmark or content section")
    for href in parser.anchors:
        if href.startswith("#") and href[1:] not in parser.ids:
            raise ValueError("Broken in-page anchor: " + href)
        if href.startswith("http://"):
            raise ValueError("Insecure external URL: " + href)
    for path in parser.stylesheets + parser.assets:
        if not path.startswith("./") or not (SITE / path).is_file():
            raise ValueError("Missing or unsafe local site asset: " + path)
    if not (SITE / ".nojekyll").exists():
        raise ValueError("Missing Pages static site marker")
    expected = (
        "https://doi.org/10.1504/IJMC.2026.154630",
        "https://www.ijisae.org/index.php/IJISAE/article/view/2010",
        "https://github.com/abyilmaz-BatuhanYILMAZ/AI-Agent-Security-Lab",
    )
    for link in expected:
        if link not in parser.anchors:
            raise ValueError("Missing verified public evidence link: " + link)
    page_text = page.read_text(encoding="utf-8")
    for marker in ("95.71", "2017", "2022", "Certified Ethical Hacker", "ISO/IEC 27001:2022", "renewal/CPE"):
        if marker not in page_text:
            raise ValueError("Missing education or qualified credential detail: " + marker)
    if not (ROOT / "docs/EDUCATION-CREDENTIALS.md").exists():
        raise ValueError("Credential caveats documentation not committed")
    if not (ROOT / "career/RED-TEAM-LEADERSHIP-CASE-STUDY.md").exists():
        raise ValueError("Professional leadership artifact not committed")
    print(f"PASS: one-page portfolio; {len(parser.ids)} unique anchors; "
          f"{len(parser.anchors)} navigation/evidence links; "
          f"{len(parser.stylesheets)+len(parser.assets)} local assets")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError) as exc:
        print(f"Portfolio site check FAILED: {exc}", file=sys.stderr)
        raise SystemExit(1)
