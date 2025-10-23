---
# Leave the homepage title empty to use the site title
title:
date: 2023-09-06
type: landing

sections:
  # Biography Section
  - block: about.biography
    id: about
    content:
      title: Biography
      username: admin

  # Audience-Specific Introduction
  - block: markdown
    content:
      title: ""
      text: |
        <div class="audience-content active" data-audience="academic" aria-hidden="false" id="academic-content">
          <div class="research-focus">
            <h3>Research at the Intersection of AI and Society</h3>
            <p>My work pioneers the application of advanced machine learning techniques—including voice activity detection (VAD), automatic speech recognition (ASR), speech emotion recognition (SER), and natural language processing (NLP)—to analyze police radio communications. This novel approach addresses a critical gap in policing research by examining the coordination and decision-making processes that occur <em>before</em> encounters with the public.</p>
            <p>Theoretically grounded in Spencer's phenomenological variant of ecological systems theory (PVEST), my research bridges computational social science and urban sociology to understand policing as a complex sociotechnical system.</p>
          </div>

          <h3>Current Research Trajectory</h3>
          <div class="key-insights">
            <div class="insight-card">
              <h4>🎯 Novel Data Sources in Policing Research</h4>
              <p>First systematic analysis of police radio transmissions using state-of-the-art ML/AI methods. This understudied data source reveals coordination patterns invisible in traditional administrative data or body camera footage.</p>
            </div>
            <div class="insight-card">
              <h4>🔬 Methodological Innovation</h4>
              <p>Development of mixed-methods approaches that combine computational analysis with ethnographic understanding, advancing translational AI that bridges technical capabilities with social science theory.</p>
            </div>
            <div class="insight-card">
              <h4>⚖️ Data Ethics & Governance</h4>
              <p>Pioneering work on participatory data governance frameworks, proposing decentralized autonomous data stewardship models that rebalance power between data subjects and data users.</p>
            </div>
          </div>
        </div>

        <div class="audience-content" data-audience="policymaker" aria-hidden="true" id="policymaker-content">
          <div class="research-focus">
            <h3>Evidence-Based Insights for Police Reform</h3>
            <p>My research provides policymakers with unprecedented access to understanding police behavior through analysis of radio communications—the primary coordination tool for officers. This work offers objective, data-driven insights into how officers make decisions, coordinate responses, and interact with communities.</p>
            <p>By analyzing patterns in hundreds of hours of radio transmissions using artificial intelligence, I identify systemic issues and opportunities for intervention that traditional metrics miss.</p>
          </div>

          <h3>Policy-Relevant Findings</h3>
          <div class="key-insights">
            <div class="insight-card">
              <h4>📊 New Metrics for Police Accountability</h4>
              <p>Radio communications data reveals officer coordination patterns, response decision-making, and resource allocation in real-time—providing accountability metrics beyond traditional complaint data or use-of-force statistics.</p>
            </div>
            <div class="insight-card">
              <h4>🛡️ Early Intervention Opportunities</h4>
              <p>Analysis of communication patterns can identify officers or units that may benefit from additional training or support, enabling proactive intervention before escalation.</p>
            </div>
            <div class="insight-card">
              <h4>🤝 Community-Centered Data Governance</h4>
              <p>Proposed frameworks for decentralized data stewardship that give communities meaningful control over how their data is collected, used, and shared—addressing power imbalances in current surveillance systems.</p>
            </div>
            <div class="insight-card">
              <h4>💡 Evidence-Based Resource Allocation</h4>
              <p>Objective analysis of dispatch patterns and response coordination helps optimize resource deployment and identify gaps in service delivery.</p>
            </div>
          </div>

          <div style="margin-top: 40px; padding: 25px; background: rgba(102, 126, 234, 0.05); border-radius: 12px; border-left: 4px solid #667eea;">
            <h4 style="margin-top: 0; color: #667eea;">Available for Consultation</h4>
            <p>I work with policymakers, community organizations, and law enforcement agencies to translate research findings into actionable policy recommendations. My approach emphasizes participatory methods that center community needs and values.</p>
          </div>
        </div>

        <div class="audience-content" data-audience="public" aria-hidden="true" id="public-content">
          <div class="research-focus">
            <h3>Using AI to Understand Policing in Your Community</h3>
            <p>When you hear police sirens or see officers responding to a call, there's an entire conversation happening over radio that guides their actions. My research uses artificial intelligence to listen to and understand these conversations, revealing how police make decisions and coordinate before they interact with community members.</p>
            <p>This work matters because it helps answer questions communities have been asking: How do police decide where to go? How do they talk about neighborhoods? What influences their decisions before they arrive at a scene?</p>
          </div>

          <h3>What This Means for Communities</h3>
          <div class="key-insights">
            <div class="insight-card">
              <h4>🔍 Transparency Through Technology</h4>
              <p>By analyzing police radio communications (which are publicly available in many cities), this research reveals patterns in policing that aren't visible in official reports. It's like having a window into how police actually work day-to-day.</p>
            </div>
            <div class="insight-card">
              <h4>👥 Your Data, Your Rights</h4>
              <p>My work on data governance asks: Who should control data about our communities? I'm developing models where communities—not corporations or government alone—have real power over how their data is used.</p>
            </div>
            <div class="insight-card">
              <h4>⚡ Ahead of the Curve</h4>
              <p>This research anticipated many current conversations about AI ethics, police accountability, and data rights. By studying these issues early, we can shape how these technologies develop rather than just reacting to problems after they arise.</p>
            </div>
            <div class="insight-card">
              <h4>🌍 Real-World Impact</h4>
              <p>The goal isn't just academic papers—it's creating tools and frameworks that help communities hold police accountable and participate meaningfully in decisions about surveillance and safety.</p>
            </div>
          </div>

          <div style="margin-top: 40px; padding: 25px; background: rgba(102, 126, 234, 0.05); border-radius: 12px; border-left: 4px solid #667eea;">
            <h4 style="margin-top: 0; color: #667eea;">Community Engagement</h4>
            <p>I believe research should serve communities, not just academic journals. If you're interested in understanding policing in your area or want to discuss participatory research approaches, I'd love to hear from you.</p>
            <p><a href="mailto:graziul@uchicago.edu" class="cta-button">Get in Touch</a></p>
          </div>
        </div>

  # Innovation Timeline - "Ahead of My Time, Every Time"
  - block: markdown
    content:
      title: "Innovation Timeline: Anticipating the Future"
      text: |
        <div class="innovation-timeline">
          <div class="timeline-item">
            <div class="timeline-year">2016-2018</div>
            <div class="timeline-title">Early Spatial Analysis & Computational Methods <span class="ahead-badge">Pioneer</span></div>
            <div class="timeline-description">Developed novel geocoding and segregation analysis methods for historic census data, applying computational approaches to urban sociology before they became mainstream in the field.</div>
          </div>

          <div class="timeline-item">
            <div class="timeline-year">2018-2020</div>
            <div class="timeline-title">Mixed Methods in STEM Education Research</div>
            <div class="timeline-description">Integrated PVEST theory with data science to assess educational interventions, pioneering theory-informed computational approaches in education research.</div>
          </div>

          <div class="timeline-item">
            <div class="timeline-year">2020-2022</div>
            <div class="timeline-title">AI Ethics in Policing <span class="ahead-badge">Pioneer</span></div>
            <div class="timeline-description">Began researching AI/ML applications in policing studies years before the mainstream conversation about AI surveillance and algorithmic accountability exploded in 2023-2024.</div>
          </div>

          <div class="timeline-item">
            <div class="timeline-year">2022-Present</div>
            <div class="timeline-title">Novel Data Sources: Radio Communications <span class="ahead-badge">First Mover</span></div>
            <div class="timeline-description">First systematic application of VAD, ASR, SER, and NLP to police radio transmissions—an entirely understudied data source that reveals coordination patterns invisible in other police data.</div>
          </div>

          <div class="timeline-item">
            <div class="timeline-year">2024-Present</div>
            <div class="timeline-title">Decentralized Data Stewardship <span class="ahead-badge">Cutting Edge</span></div>
            <div class="timeline-description">Developing participatory data governance frameworks and proposing decentralized autonomous data stewardship models—anticipating the next evolution in data rights and community control.</div>
          </div>
        </div>

  # Recent Work & Impact
  - block: markdown
    content:
      title: "Recent Work"
      text: |
        <div class="publications-enhanced">
          <div class="publication-card">
            <span class="publication-type">CONFERENCE • ICML 2025</span>
            <div class="publication-title">BPC-CPD: A Large-scale Corpus of Broadcast Police Communications Categorized by Police Department</div>
            <div class="publication-meta">
              OpenReview • Machine Learning Conference
            </div>
            <p>Novel corpus of police radio communications with detailed categorization—enabling research on police coordination patterns, dispatch systems, and communication strategies across departments.</p>
            <div class="audience-content active" data-audience="academic">
              <div class="audience-relevance">
                <strong>Academic Relevance:</strong> First large-scale corpus for studying police communications as data. Enables research in NLP, speech processing, sociolinguistics, and computational social science.
              </div>
            </div>
            <div class="audience-content" data-audience="policymaker">
              <div class="audience-relevance">
                <strong>Policy Relevance:</strong> Provides standardized data infrastructure for comparing police practices across departments, enabling evidence-based policy development and accountability measures.
              </div>
            </div>
            <div class="audience-content" data-audience="public">
              <div class="audience-relevance">
                <strong>Why It Matters:</strong> Creates a public resource that helps communities and researchers understand how police communicate and coordinate—making police practices more transparent.
              </div>
            </div>
            <a href="https://openreview.net/forum?id=Cra2VWhYfR" target="_blank" class="cta-button" style="margin-top: 15px;">View Paper</a>
          </div>

          <div class="publication-card">
            <span class="publication-type">CONFERENCE • CSCW 2024</span>
            <div class="publication-title">Computer-Supported Cooperative Work Research</div>
            <div class="publication-meta">
              ACM Conference on Computer-Supported Cooperative Work and Social Computing
            </div>
            <p>Examining sociotechnical systems in policing and how technology mediates coordination and decision-making among officers.</p>
            <div class="audience-content active" data-audience="academic">
              <div class="audience-relevance">
                <strong>Academic Relevance:</strong> Bridges HCI, CSCW, and criminology to understand police radio as a sociotechnical system—expanding CSCW research into public safety domains.
              </div>
            </div>
            <div class="audience-content" data-audience="policymaker">
              <div class="audience-relevance">
                <strong>Policy Relevance:</strong> Reveals how communication technologies shape police behavior, informing decisions about technology adoption and training in law enforcement agencies.
              </div>
            </div>
            <div class="audience-content" data-audience="public">
              <div class="audience-relevance">
                <strong>Why It Matters:</strong> Helps us understand how police technology affects community interactions—important for debates about police surveillance and accountability tools.
              </div>
            </div>
            <a href="https://dl.acm.org/doi/10.1145/3641057" target="_blank" class="cta-button" style="margin-top: 15px;">View Paper</a>
          </div>

          <div class="publication-card">
            <span class="publication-type">CONFERENCE • SLT 2024</span>
            <div class="publication-title">Spoken Language Technologies for Police Communications</div>
            <div class="publication-meta">
              IEEE Workshop on Spoken Language Technology
            </div>
            <p>Developing and evaluating speech processing models (ASR, SER) specifically designed for police radio communications—a challenging domain with unique acoustic properties and terminology.</p>
            <div class="audience-content active" data-audience="academic">
              <div class="audience-relevance">
                <strong>Academic Relevance:</strong> Advances speech processing research with a novel domain application, contributing new benchmarks and methods for processing radio communications.
              </div>
            </div>
            <div class="audience-content" data-audience="policymaker">
              <div class="audience-relevance">
                <strong>Policy Relevance:</strong> Creates technical infrastructure for automated analysis of police communications, enabling scalable oversight and quality assurance systems.
              </div>
            </div>
            <div class="audience-content" data-audience="public">
              <div class="audience-relevance">
                <strong>Why It Matters:</strong> Develops tools that can automatically analyze thousands of hours of police radio—making oversight practical at a scale that would be impossible with human reviewers alone.
              </div>
            </div>
            <a href="https://ieeexplore.ieee.org/document/10740567" target="_blank" class="cta-button" style="margin-top: 15px;">View Paper</a>
          </div>

          <div class="publication-card">
            <span class="publication-type">JOURNAL ARTICLE • 2020</span>
            <div class="publication-title">Neighborhood formation in St. Louis, 1930</div>
            <div class="publication-meta">
              Environment and Planning B: Urban Analytics and City Science • With John Logan & Nathan Frey
            </div>
            <p>Historical spatial analysis of neighborhood formation using novel geocoding methods for full-count census data, revealing patterns of residential segregation in early 20th century American cities.</p>
            <div class="audience-content active" data-audience="academic">
              <div class="audience-relevance">
                <strong>Academic Relevance:</strong> Methodological contribution to urban sociology and historical GIS, demonstrating how computational methods enable new analyses of historical segregation patterns.
              </div>
            </div>
            <div class="audience-content" data-audience="policymaker">
              <div class="audience-relevance">
                <strong>Policy Relevance:</strong> Provides historical context for understanding present-day urban inequality and segregation, informing contemporary housing and urban planning policies.
              </div>
            </div>
            <div class="audience-content" data-audience="public">
              <div class="audience-relevance">
                <strong>Why It Matters:</strong> Shows how neighborhoods were deliberately segregated in the past—helping us understand why cities look the way they do today and what that means for fairness and opportunity.
              </div>
            </div>
            <a href="https://doi.org/10.1177/2399808318801958" target="_blank" class="cta-button" style="margin-top: 15px;">Read Article</a>
          </div>
        </div>

  # Experience Section
  - block: experience
    content:
      title: Experience
      date_format: Jan 2006
      items:
        - title: Research Assistant Professor
          company: University of Chicago
          company_url: ''
          company_logo: UChicago_Avatar
          location: Illinois
          date_start: '2022-08-01'
          date_end: ''
          description: |2-
            Leading development of AI/ML methods for analyzing police communications and mentoring interdisciplinary research teams.

            * Direct VAD, ASR, SER, and NLP development for police radio analysis
            * Lead manuscript development across multiple disciplines
            * Mentor 15-20 graduate research assistants in theory-based data science

        - title: Data Scientist
          company: University of Chicago
          company_url: ''
          company_logo: UChicago_Avatar
          location: Illinois
          date_start: '2018-07-01'
          date_end: '2022-07-31'
          description: |2-
            Mixed methods research bridging education, urban studies, and computational social science.

            * Developed PVEST-informed research designs for NSF STEM-US Center
            * Assessed arts-augmented STEM curricula effectiveness
            * Led IRB protocols, experimental design, and secondary data analysis

        - title: Postdoctoral Research Fellow
          company: Brown University
          company_url: ''
          company_logo: Brown_Avatar
          location: Rhode Island
          date_start: '2016-07-01'
          date_end: '2018-06-29'
          description: |2-
            Computational historical geography and segregation analysis.

            * Geocoded full-count census data (1900-1940) for 69 cities
            * Developed novel segregation measures for point-level data
            * Built scalable ETL workflows processing 30M+ records
    design:
      columns: '2'

  # Impact Metrics
  - block: markdown
    content:
      title: ""
      text: |
        <div class="impact-grid">
          <div class="impact-card">
            <div class="impact-number">4</div>
            <div class="impact-label">Major Conferences (2024-25)</div>
          </div>
          <div class="impact-card">
            <div class="impact-number">15-20</div>
            <div class="impact-label">Graduate RAs Mentored</div>
          </div>
          <div class="impact-card">
            <div class="impact-number">10+</div>
            <div class="impact-label">Years Computational Research</div>
          </div>
          <div class="impact-card">
            <div class="impact-number">3</div>
            <div class="impact-label">Disciplines Bridged</div>
          </div>
        </div>

  # Resources Section
  - block: markdown
    id: resources
    content:
      title: "Resources & Links"
      text: |
        <div class="publications-enhanced">
          <div class="publication-card">
            <span class="publication-type">DATASET</span>
            <div class="publication-title">BPC-CPD Corpus</div>
            <div class="publication-meta">
              Large-scale corpus of broadcast police communications
            </div>
            <p>A comprehensive dataset of police radio communications, categorized by department and annotated for research purposes. This open resource enables researchers, policymakers, and communities to study police coordination patterns.</p>
            <a href="https://voices.uchicago.edu/p2r/bpc-cpd-corpus/" target="_blank" class="cta-button" style="margin-top: 15px;">Access Dataset</a>
          </div>

          <div class="publication-card">
            <span class="publication-type">PROFILES</span>
            <div class="publication-title">Academic & Professional Profiles</div>
            <p>Find me on academic networks and professional platforms:</p>
            <div style="margin-top: 15px; display: flex; gap: 10px; flex-wrap: wrap;">
              <a href="https://scholar.google.com/citations?user=OQr5RwsAAAAJ" target="_blank" class="cta-button">Google Scholar</a>
              <a href="https://orcid.org/0000-0001-8350-077X" target="_blank" class="cta-button">ORCID</a>
              <a href="https://www.linkedin.com/in/christopher-graziul-6250344/" target="_blank" class="cta-button">LinkedIn</a>
              <a href="https://twitter.com/cgraziul" target="_blank" class="cta-button">Twitter</a>
            </div>
          </div>

          <div class="publication-card">
            <span class="publication-type">CONTACT</span>
            <div class="publication-title">Get in Touch</div>
            <p>I'm available for:</p>
            <ul style="margin: 15px 0; padding-left: 25px; line-height: 1.8;">
              <li><strong>Academic Collaborations:</strong> Research partnerships, co-authoring, data sharing</li>
              <li><strong>Policy Consulting:</strong> Evidence-based policy development, data governance frameworks</li>
              <li><strong>Community Engagement:</strong> Participatory research design, public talks, workshops</li>
              <li><strong>Time-Bounded Projects:</strong> Specific research questions or technical challenges</li>
              <li><strong>Tenure-Track Opportunities:</strong> Currently on the job market for faculty positions</li>
            </ul>
            <a href="mailto:graziul@uchicago.edu" class="cta-button" style="margin-top: 15px;">Email Me</a>
          </div>
        </div>
---
