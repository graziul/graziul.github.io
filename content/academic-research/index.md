---
title: Academic Research
date: 2026-01-01
type: page
---

## Policing as a Sociotechnical System

Before I could study police radio, I had to invent the governance for studying it. No framework existed for data that was legally public but contained personal information about people who never consented to being studied.

The foundation of this research program is the BPC-CPD corpus: 62,080 manually transcribed utterances drawn from roughly 30,000 hours of Chicago Police Department radio archives, totaling approximately 46.2 hours of speech. It is the first corpus of its kind — built not because the raw recordings were hard to obtain, but because no research infrastructure, no governance model, and no analytical toolchain existed for working with them responsibly at scale. Building that infrastructure was most of the work.

**The NIH project.** The first major analysis came through NIH R01MD015064, funded by the National Institute on Minority Health and Health Disparities. The project, led by PI Margaret Beale Spencer under her Phenomenological Variant of Ecological Systems Theory (PVEST) framework, conducted the first systematic analysis of procedural language in broadcast police communications. I led data infrastructure and machine learning modeling across the project, and mentored 15–20 graduate research assistants in methods ranging from corpus annotation to model evaluation.

**Speech recognition.** Off-the-shelf automatic speech recognition models fail badly on police radio. The acoustic environment is noisy, the vocabulary is domain-specific, and the speaking style is compressed and procedural. We fine-tuned existing ASR models on the BPC-CPD corpus and showed that domain-adapted models approach human transcription performance — a necessary step before any large-scale linguistic analysis is computationally feasible. Published at SLT 2024 (Srivastava, Chou, Shroff, Livescu & Graziul, arXiv:2409.10858).

**Race and privacy.** The most consequential paper from this program documented a clear, systematic pattern: CPD professionals disproportionately mention Black individuals regardless of neighborhood racial composition, criminal context, or call type. Males are mentioned approximately nine times more often than females. These patterns hold even in majority-white zones, where the demographic asymmetry in police speech cannot be explained by the local population. The paper won the CSCW 2024 DEI Award (Venkit, Graziul et al., DOI:10.1145/3686921).

**Sensitive open data.** The governance problems raised by this research do not fit neatly into existing frameworks. The data is not proprietary — it was broadcast on public radio frequencies by a public agency. But it contains personal information about individuals who had no say in whether they would appear in a research corpus. In *Katina Magazine* (January 2026), Danton and I proposed the concept of "sensitive open data" — publicly mandated, legally unrestricted, yet privacy-sensitive material — and argued that governing it requires new institutional frameworks rather than incremental extensions of existing ones.

**The institutional case.** The logical endpoint of this work is a national repository of policing data: professionally curated, historically preserved, responsibly governed, and accessible to researchers, policymakers, and communities. I followed the institutional path as far as it would go — making the formal case in a white paper archived in the Knowledge@UChicago repository (Graziul, Danton & Ramos, record 15600, 2024). The community-facing complement to that institutional argument is [IDEP](https://idep.org) — the Illinois Data Equity Project — which provides tools and governance infrastructure for the communities most affected by data-driven systems.

**Key publications:**

- Venkit, Graziul et al. (2024). "Race and Privacy in Broadcast Police Communications." *PACM HCI* 8(CSCW2). **CSCW 2024 DEI Award.** [DOI:10.1145/3686921](https://dl.acm.org/doi/10.1145/3686921)
- Srivastava, Chou, Shroff, Livescu & Graziul (2024). "Speech Recognition for Analysis of Police Radio Communication." arXiv:2409.10858. *SLT 2024*, pp. 906–912.
- Danton & Graziul (2026). "Confronting the Challenges of Sensitive Open Data." *Katina Magazine*, January.
- Graziul, Danton & Ramos (2024). "The Case for a National Repository of Policing Data." *Knowledge@UChicago* record 15600.

---

## The Broader Arc

The combination — physics, sociology, GIS, ML, community organizing — isn't magic. It's the result of asking at every stage: what do I need to understand this problem properly?

**Physics & Mathematics (Virginia Tech, 2004)**

Two B.S. degrees because complex system dynamics required both. The technical training gave me the willingness to bring quantitative methods to social problems and the patience for projects that take a decade to come into focus. By the time I graduated, it was already clear that the questions worth answering were not going to be physics questions. The substantive lessons from sociology — about how institutions actually behave when nobody is watching, and about whose interests the technical answer tends to serve — are what make the technical training safe to deploy.

**GIS & Historical Data (Brown University, 2016–2018)**

As a postdoc at Brown's Population Studies and Training Center, I geocoded full-count census data for 69 U.S. cities spanning 1900 to 1940, as part of John R. Logan's Urban Transition Historical GIS Project. For 1930 alone, this involved roughly 30 million records. The core challenge was not the volume but the consistency: historical addresses are ambiguous, street grids have changed, and the source data was collected by humans who were not thinking about computational processing. The key publication from that work is Logan, Graziul & Frey (2018), "Neighborhood Formation in St. Louis, 1930," *Environment and Planning B* 45(6). GIS has run as connective tissue through all subsequent work — historical segregation, policing geography, and the spatial infrastructure underlying IDEP's community maps.

**Urban Sociology & Scenes (University of Chicago, 2005–2016)**

The "scenes" framework examines how cultural amenities — restaurants, music venues, galleries, community spaces — generate social bonds and political resources. My dissertation and related publications developed the quantitative infrastructure for measuring scene types across U.S. cities and analyzing their relationship to voting behavior, social movement formation, and neighborhood change. Publications include Silver, Clark & Graziul (2011) in the *Handbook of Creative Cities* (Edward Elgar); my chapter in *Scenescapes* (Silver & Clark eds., University of Chicago Press, 2016); and Silver, Graziul & Clark (2013), SSRN 2318302. Understanding how communities organize around shared cultural spaces became a direct foundation for thinking about how online communities form and self-govern — the theoretical lens I brought to the work I later did inside CEDR.

**DARPA Ground Truth (~2023)**

As part of a large multi-institution collaboration, our team tested social science methods against simulated social worlds where the causal structure was known in advance. The results were sobering: big data methods consistently failed to recover the true causal structure from observational data alone. The key finding — that big data requires contextual knowledge to be interpretively valid, and that contemporary quantitative social science cannot reliably recover causal structure without it — is published as Graziul et al. (2023), "Does big data serve policy? Not without context," *Computational and Mathematical Organization Theory* 29(1), 188–219. This is peer-reviewed empirical grounding for skepticism about the idea that we can measure our way to good AI governance. The data exists; the question is whether we know how to read it.
