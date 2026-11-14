# Publish this portfolio on GitHub Pages and a .dev domain

## Fix the current GitHub Pages custom domain error

The error shown for `batuhanyilmaz.github.io/publications/` means that a **URL path** was entered into GitHub Pages **Custom domain**. A custom domain entry accepts a **hostname only** (e.g. `batuhanyilmaz.dev`), not a URL or slash path.

For this `Publications` repository:

1. Visit **Settings → Pages** and clear/remove the invalid Custom domain.
2. Choose **Build and deployment → Deploy from a branch → main /docs**.
3. Open the GitHub-generated Pages URL displayed after deployment. Expected if the account is `abyilmaz-BatuhanYILMAZ`: `https://abyilmaz-batuhanyilmaz.github.io/Publications/`.

Do not put the URL above into the **Custom domain** field.

## User site without /Publications/

A dedicated user site must be in a repository named **`abyilmaz-batuhanyilmaz.github.io`** (the lowercase GitHub account name), using the site files as root content. The expected default site URL is then `https://abyilmaz-batuhanyilmaz.github.io/`.

The exact default URL `https://batuhanyilmaz.github.io/` is **not available under a different GitHub username** simply by entering it as a custom domain. Changing the GitHub username (if available) or using a GitHub account with that username is a separate decision with repository and link implications.

## Custom .dev domain without changing GitHub username

A personally registered `batuhanyilmaz.dev` can point to GitHub Pages regardless of GitHub username, if the domain is available and the holder controls the registrar's DNS zone.

**Student Pack option:** As listed in the [GitHub Student Developer Pack](https://education.github.com/pack), Name.com offers a **selected free domain** among multiple extensions including **.dev** for eligible students. Domain-name availability, eligibility, redemption duration, renewal price and premium-name exclusions must be checked before claiming or purchasing. This is not a universal free `.dev` entitlement of GitHub Pro itself.

If the root `batuhanyilmaz.dev` domain is registered, configure the registrar's DNS records according to the current [official GitHub Pages custom-domain documentation](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site); for an **apex** domain GitHub documents A records:

```text
@  A  185.199.108.153
@  A  185.199.109.153
@  A  185.199.110.153
@  A  185.199.111.153
```

Optionally add `www` as a CNAME to `abyilmaz-batuhanyilmaz.github.io` (not a path). Do not create conflicting A/AAAA/CNAME records. For a subdomain only, use a CNAME matching the docs.

Then set **Custom domain = batuhanyilmaz.dev** in GitHub Pages, verify domain ownership using GitHub's Settings/domain verification workflow as offered, wait for DNS/Pages provisioning, and enable **Enforce HTTPS** once the certificate is ready. The `.dev` TLD requires HTTPS for normal browsing. A domain purchase and DNS edit have **not** been performed by this repository.

**Important:** Site source files are stored in `/docs` with relative stylesheet/favicon references and can be moved to a user-site repository later without rewriting the entire page.
