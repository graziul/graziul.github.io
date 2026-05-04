---
title: Academic Research
date: 2026-01-01
type: page
share: false
commentable: false
---

## Policing as a Sociotechnical System

Before I could study police radio, I had to invent the governance for studying it. No framework existed for data that was legally public but contained personal information about people who never consented to being studied.

The foundation of this research program is the BPC-CPD corpus: 62,080 manually transcribed utterances drawn from roughly 30,000 hours of Chicago Police Department radio archives, totaling approximately 46.2 hours of speech. It is the first corpus of its kind — built not because the raw recordings were hard to obtain, but because no research infrastructure, no governance model, and no analytical toolchain existed for working with them responsibly at scale. Building that infrastructure was most of the work.

### Origins in spatial mortality work

Before the radio data was a research program, it was a hypothesis: that the geography of police–civilian interactions, and the language of those interactions, was patterned in ways the existing literature had not yet measured. The earliest piece of work in that direction was a 2017 PAA paper with Bonnie Bellman, Manuel Martinez, and John Logan — *Spatial and social contexts of mortality resulting from interactions with police* — which used GIS methods to examine where fatal police encounters concentrate and what neighborhood characteristics predict them. That paper is the bridge between my earlier GIS infrastructure work at Brown and the NIH program that followed.

### The NIH project

The first major analysis came through NIH R01MD015064, a $2.66M award from the National Institute on Minority Health and Health Disparities. I served as co-PI alongside Margaret Beale Spencer, whose Phenomenological Variant of Ecological Systems Theory (PVEST) framed the study, and led the data infrastructure and machine-learning modeling across the project. Roughly 50 graduate research assistants moved through the project across its life — annotating the corpus, evaluating models, running domain-specific subprojects, and learning the methods involved.

### Speech recognition

Off-the-shelf automatic speech recognition models fail badly on police radio. The acoustic environment is noisy, the vocabulary is domain-specific, and the speaking style is compressed and procedural. We fine-tuned existing ASR models on the BPC-CPD corpus and showed that domain-adapted models approach human transcription performance — a necessary step before any large-scale linguistic analysis is computationally feasible. Published at SLT 2024 (Srivastava, Chou, Shroff, Livescu & Graziul, [arXiv:2409.10858](https://arxiv.org/abs/2409.10858)).

### Race and privacy

The most consequential paper from this program documented a clear, systematic pattern: CPD professionals disproportionately mention Black individuals regardless of neighborhood racial composition, criminal context, or call type. Males are mentioned approximately nine times more often than females. These patterns hold even in majority-white zones, where the demographic asymmetry in police speech cannot be explained by the local population. The paper won the **CSCW 2024 DEI Award** (Venkit, Graziul et al., [doi:10.1145/3686921](https://doi.org/10.1145/3686921)).

### Sensitive open data

The governance problems raised by this research do not fit neatly into existing frameworks. The data is not proprietary — it was broadcast on public radio frequencies by a public agency. But it contains personal information about individuals who had no say in whether they would appear in a research corpus. In *Katina Magazine* (January 2026), Danton and I proposed the concept of "sensitive open data" — publicly mandated, legally unrestricted, yet privacy-sensitive material — and argued that governing it requires new institutional frameworks rather than incremental extensions of existing ones.

### The institutional case

The logical endpoint of this work is a national repository of policing data: professionally curated, historically preserved, responsibly governed, and accessible to researchers, policymakers, and communities. I followed the institutional path as far as it would go — making the formal case in a 2025 paper presented at the International Conference on Open Repositories (Danton, Graziul & Ramos, [doi:10.5281/zenodo.15758688](https://doi.org/10.5281/zenodo.15758688)). The community-facing complement to that institutional argument is [IDEP](https://idep.org) — the Illinois Data Equity Project — which provides tools and governance infrastructure for the communities most affected by data-driven systems.

---

## The Broader Arc

The combination — physics, sociology, GIS, ML, community organizing — isn't magic. It's the result of asking at every stage: what do I need to understand this problem properly?

### Physics & Mathematics
*Virginia Tech, 2004*

Two B.S. degrees because complex system dynamics required both. The technical training gave me the willingness to bring quantitative methods to social problems and the patience for projects that take a decade to come into focus. By the time I graduated, it was already clear that the questions worth answering were not going to be physics questions. The substantive lessons from sociology — about how institutions actually behave when nobody is watching, and about whose interests the technical answer tends to serve — are what make the technical training safe to deploy.

### GIS & Historical Data
*Brown University, 2016–2018*

As a postdoc at Brown's Population Studies and Training Center, I geocoded full-count census data for 69 U.S. cities spanning 1900 to 1940, as part of John R. Logan's Urban Transition Historical GIS Project. For 1930 alone, this involved roughly 30 million records. The core challenge was not the volume but the consistency: historical addresses are ambiguous, street grids have changed, and the source data was collected by humans who were not thinking about computational processing. The key publication from that work is Logan, Graziul & Frey (2018), "Neighborhood Formation in St. Louis, 1930," *Environment and Planning B* 45(6) ([doi:10.1177/2399808318801958](https://doi.org/10.1177/2399808318801958)). GIS has run as connective tissue through all subsequent work — historical segregation, policing geography, and the spatial infrastructure underlying IDEP's community maps.

### Urban Sociology & Scenes
*University of Chicago, 2005–2016*

The "scenes" framework examines how cultural amenities — restaurants, music venues, galleries, community spaces — generate social bonds and political resources. My dissertation and related publications developed the quantitative infrastructure for measuring scene types across U.S. cities and analyzing their relationship to voting behavior, social movement formation, and neighborhood change. The capstone is my co-authored chapter in *Scenescapes* (Silver, Clark & Graziul, "The Science of Scenes," University of Chicago Press, 2016). Understanding how communities organize around shared cultural spaces became a direct foundation for thinking about how online communities form and self-govern — the theoretical lens I brought to the work I later did inside CEDR.

### DARPA Ground Truth
*Multi-institution collaboration, ~2023*

As part of a large multi-institution collaboration, our team tested social science methods against simulated social worlds where the causal structure was known in advance. The results were sobering: big data methods consistently failed to recover the true causal structure from observational data alone. The key finding — that big data requires contextual knowledge to be interpretively valid, and that contemporary quantitative social science cannot reliably recover causal structure without it — is published as Graziul et al. (2023), "Does big data serve policy? Not without context," *Computational and Mathematical Organization Theory* 29(1), 188–219 ([doi:10.1007/s10588-022-09362-3](https://doi.org/10.1007/s10588-022-09362-3)). This is peer-reviewed empirical grounding for skepticism about the idea that we can measure our way to good AI governance. The data exists; the question is whether we know how to read it.
