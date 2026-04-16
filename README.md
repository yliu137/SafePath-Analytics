# SafePath Analytics
**A Privacy-Preserving Causal Inference Framework for Independent Algorithmic Auditing.**

[Read the Technical Whitepaper (PDF)](./docs/SafePath_Analytics_Whitepaper.pdf)

## Motivation
There is a massive information asymmetry between proprietary social media platforms and the public sector. While recommendation systems are aggressively optimized for engagement, public institutions (schools, youth NGOs, policymakers) lack the technical infrastructure to independently audit the long-term well-being outcomes of these algorithms on vulnerable populations, particularly teens. 

## The Problem Space
Current digital safety measures are fundamentally reactive and inadequate because:
- **The Black Box Effect:** Public institutions cannot link content exposure to downstream behavioral outcomes without access to proprietary platform data.
- **Lack of Causal Rigor:** Existing school monitoring tools rely on crude correlations rather than causal inference, failing to identify algorithmically induced "rabbit holes."
- **Privacy Bottlenecks:** Analyzing student digital behavior traditionally risks violating strict privacy laws (e.g., FERPA/COPPA), preventing meaningful data collection at the local level.

## Technical Approach
This project disrupts the current market failure by deploying a decentralized, privacy-first analytics pipeline at the edge (e.g., within a school's IT boundary). The core architecture combines:
- **$\epsilon$-Differential Privacy ($\epsilon$-DP):** Irreversibly sanitizes digital telemetry at the local edge, mathematically guaranteeing FERPA compliance and ensuring zero risk of individual student re-identification.
- **Causal Inference Engine:** Utilizes Propensity Score Matching (PSM) and Difference-in-Differences (DiD) on observational data to isolate the true causal impact of algorithmic exposure.
- **Small-Sample Causal Estimation:** Utilizes robust estimators to derive high-confidence intervention signals for educational pilots without requiring massive, platform-scale datasets.
- **Content Benchmarking:** Leverages multi-modal LLMs to classify and benchmark recommendation feedback loops without human-in-the-loop privacy breaches.

## Core Use Case: The "Late-Night Rabbit Hole" Audit
- **Input:** DP-sanitized network telemetry identifying an algorithmic shift (e.g., from educational content to high-arousal short videos after 10:00 PM).
- **Process:** The Causal Engine isolates this sequence and compares downstream engagement duration against a synthetic control group.
- **Output:** A statistically rigorous "$p < 0.01$ Algorithmic Hazard Alert," empowering schools to justify local firewall throttling based on causal harm, rather than anecdotal evidence.

## The Goal
Not to serve the platforms, but to **empower the public sector**. This toolkit provides public schools, independent researchers, and youth-advocacy organizations with a **regulatory-grade** analytics layer to scientifically audit algorithmic harm, enforce digital safety policies, and protect youth mental health.
