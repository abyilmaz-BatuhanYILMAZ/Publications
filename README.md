# Research Publications | Abdullah Batuhan Yilmaz

**Peer-reviewed research in Android malware detection, machine learning, and application security.**

This repository is a curated academic publication record. It provides verified bibliographic information, publisher links, research summaries, and machine-readable citations for two co-authored journal articles. The papers' results are **reported research results**, not experiments run by this repository.

[![Publications](https://img.shields.io/badge/peer--reviewed%20papers-2-224488)](./publications.json)
[![Research focus](https://img.shields.io/badge/research-Android%20Malware%20%7C%20Machine%20Learning-446699)](#research-areas)

## Professional portfolio website (GitHub Pages)

A responsive, English-language portfolio is prepared in [docs/index.html](docs/index.html), with accompanying [CSS](docs/style.css) and SVG favicon. It presents Red Team leadership, AI agent security research, Kubernetes and Active Directory engineering, and peer-reviewed research with conservative evidence statements.

**Publishing is a separate GitHub repository setting.** In this repository choose **Settings → Pages → Build and deployment → Deploy from a branch → main /docs → Save**. Once GitHub enables the site, the expected project URL is:

`https://abyilmaz-batuhanyilmaz.github.io/Publications/`

Do **not** treat this as a confirmed live URL until the Pages deployment succeeds. The site uses relative paths and has no external script/font dependencies; its HTML/CSS can later be moved into a dedicated `abyilmaz-batuhanyilmaz.github.io` user-site repository. A separately registered `.io` custom domain may also be attached later.

### Education, certifications and training

- **B.Sc. Computer Engineering**, Selçuk University, graduation 2017.
- **M.Sc. Computer Engineering (thesis-based)**, Selçuk University, graduation 2022, **95.71/100**; thesis **“Detection of Malicious Android Applications with Machine Learning Methods”** ([YÖK detail link from prior CV](https://tez.yok.gov.tr/UlusalTezMerkezi/tezDetay.jsp?id=PEa7Fo7NAdzpcXKpkXkMNA), current accessibility not verified).
- **CEH (Practical)**, awarded 2025 — official renewal standing not independently verified.
- **ISO/IEC 27001:2022 Auditor/Lead Auditor Course**, CTR Academy, 40 hours, completed 2024.
- [Source and evidence limitations](docs/EDUCATION-CREDENTIALS.md). Credential scans and serial numbers are **not** published.

### Professional background (public, non-confidential)

- [Red Team leadership methodology case study](career/RED-TEAM-LEADERSHIP-CASE-STUDY.md) — explicitly **not** a claimed customer engagement.
- [English professional research profile](career/PROFESSIONAL-PROFILE.md) — public statement and evidence map.
- [Interview preparation guide](career/INTERVIEW-TALKING-POINTS.md) — actual evidence, limitations and prompts for truthful case examples.

The security-career facts of nine years and current Red Team leadership were provided by the maintainer. Unverified impact metrics and client engagements are not included.

## Publications

### 2026 | Machine Learning & Feature Selection for Android Malware Detection

**Classification of malicious android applications by machine learning methods using permission properties**

*Abdullah Batuhan Yilmaz, Yavuz Selim Taspinar, Murat Koklu*

**International Journal of Mobile Communications**, 28(1), 1–22 (2026).

**[Publisher / DOI](https://doi.org/10.1504/IJMC.2026.154630)** · [Research details](papers/2026-android-malware-ml-feature-selection.md) · [BibTeX](references.bib)

**Methods:** AdaBoost, Random Forest, artificial neural networks (ANN), and information-gain feature selection.

**Dataset reported:** 2,854 malicious and 2,870 benign Android applications; evaluations with 117, 60 and 20 features.

**Reported result:** Best accuracy of **98.4%** with ANN using the complete 117-feature representation.

The article studies how permission-based feature selection changes malicious/benign Android application classification and examines metrics including precision, recall, F1, ROC/AUC and training/testing time.

### 2022 | Naive Bayes & SVM for Android Malware Classification

**Classification of Malicious Android Applications Using Naive Bayes and Support Vector Machine Algorithms**

*Abdullah Batuhan Yilmaz, Yavuz Selim Taspinar, Murat Koklu*

**International Journal of Intelligent Systems and Applications in Engineering**, 10(2), 269–274 (2022).

**[Official journal article](https://www.ijisae.org/index.php/IJISAE/article/view/2010)** · [Research details](papers/2022-android-malware-naive-bayes-svm.md) · [BibTeX](references.bib)

**Methods:** Naive Bayes (NB) and support vector machine (SVM), evaluated with 10-fold cross-validation.

**Dataset reported:** 2,854 malicious and 2,870 benign Android applications, represented by 116 permission features and a class label.

**Reported results:** **92.4%** accuracy for Naive Bayes; **90.9%** for SVM.

## Research areas

- Android application security and malware detection.
- Static permission-based feature representations.
- Machine learning for cybersecurity.
- Feature selection, model comparison and evaluation methodology.
- Reproducible security research and trustworthy measurement.

## Research timeline

| Year | Focus | Methods | Best accuracy reported in the article |
| --- | --- | --- | --- |
| **2022** | Permission-based Android malware classification | NB, SVM | 92.4% — NB |
| **2026** | ML classification with feature selection | AdaBoost, RF, ANN, information gain | 98.4% — ANN, all 117 features |

**The two accuracy figures must not be used as a direct head-to-head performance improvement.** They belong to different papers and evaluation protocols; comparable data splits, leakage controls and training configurations would need independent examination before making such a claim.

## Citations and verification

- [**BibTeX references**](references.bib) — import into a citation manager or LaTeX bibliography.
- [**Machine-readable publication metadata**](publications.json) — structured bibliography for portfolio websites.
- [**2026 journal / DOI**](https://doi.org/10.1504/IJMC.2026.154630)
- [**2022 journal article**](https://www.ijisae.org/index.php/IJISAE/article/view/2010)
- [**Author ORCID**](https://orcid.org/0000-0002-4400-712X) — listed on the 2022 journal's author page.

The 2026 article has a confirmed publisher DOI. For the 2022 paper, this repository uses the official journal URL rather than assigning an unverified DOI.

## Related security research

- [AI Agent Security Lab](https://github.com/abyilmaz-BatuhanYILMAZ/AI-Agent-Security-Lab) — separate, experimental research on prompt injection and agent tool authorization.
- [VulnWebpage](https://github.com/abyilmaz-BatuhanYILMAZ/VulnWebpage) — practical web application security training.

Those repositories are **independent projects**. Neither is presented as source code for the 2022 or 2026 journal experiments.

## Scope and research integrity

This is a **publication and citation portfolio**, not a reproduction package. It does not contain the original APK dataset, malware samples, model checkpoints, trained models, or the original experimental source code. Such materials are not implied to be available or reproducible from this repository.

To access the publications, use their official publisher or journal pages. Publisher PDFs are **not** copied into this repository; access and reuse are subject to each journal's terms. Summaries here are original paraphrases and may be updated to reflect corrections from the source articles.

See [source and interpretation notes](papers/RESEARCH-NOTES.md).
