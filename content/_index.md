---
# Leave the homepage title empty to use the site title
title:
date: 2023-09-06
type: landing

sections:
  - block: about.biography
    id: about
    content:
      title: Biography
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: admin
#  - block: features
#    content:
#      title: Skills
#      items:
#        - name: R
#          description: 80%
#          icon: r-project
#          icon_pack: fab
#        - name: Python
#          description: 80%
#          icon: python
#          icon_pack: fab
#        - name: Statistics
#          description: 100%
#          icon: chart-line
#          icon_pack: fas
  - block: experience
    content:
      title: Experience
      # Date format for experience
      #   Refer to https://wowchemy.com/docs/customization/#date-format
      date_format: Jan 2006
      # Experiences.
      #   Add/remove as many `experience` items below as you like.
      #   Required fields are `title`, `company`, and `date_start`.
      #   Leave `date_end` empty if it's your current employer.
      #   Begin multi-line descriptions with YAML's `|2-` multi-line prefix.
      items:
        - title: Research Assisant Professor
          company: University of Chicago
          company_url: ''
          company_logo: UChicago_Avatar
          location: Illinois
          date_start: '2022-08-01'
          date_end: ''
          description: |2-
            Responsibilities include:

            * Direct and oversee development of voice activity detection (VAD), automatic speech recognition (ASR), speech emotion recognition (SER), and natural language processing (NLP) strategies to determine the viability of using publicly available broadcast police communications to understand police behavior via Spencer's phenomenological variant of ecological systems theory (PVEST). 
            * Direct all aspects of manuscript development, from ideation to submission, across relevant fields and publication venues.
            * Mentor 15-20 (graduate) research assistants engaged in qualitative, quantitative, and computational tasks supporting theory-based data science 
        - title: Data Scientist
          company: University of Chicago
          company_url: ''
          company_logo: UChicago_Avatar
          location: Illinois
          date_start: '2018-07-01'
          date_end: '2022-07-31'
          description: |2-
            Responsibilities included: 
            
            All aspects of quantitative and mixed methods research projects, including but not limited to production of IRB protocols, secondary data analysis, and experiment design, in service of the Urban Resiliency Initiative and in collaboration with on-site and off-site research teams.

            * Supported development of PVEST-informed mixed methods based research designs
            * Developed a high-level PVEST-based research strategy for the NSF-funded STEM-US Center
            * Assessed efficacy of an arts-augmented STEM curriculum on academic performance of 7th-8th graders
            * Evaluated assessment tool to identify the needs of HBCU STEM students in order to improve success of HBCU students in STEM careers 
            * Contributed to multiple successfully funded grants to conduct transdisciplinary research between education researchers, social scientists, computer scientists, and physical scientists

        - title: Postdoctoral Research Fellow
          company: Brown University
          company_url: ''
          company_logo: Brown_Avatar
          location: Rhode Island
          date_start: '2016-07-01'
          date_end: '2018-06-29'
          description: |2-

              Objective: Geocode full count census data from 1900 to 1940 for 69 cities
              
              * Calculate residential segregation measures via point, line, and polygon data      
              * Assess state-of-the-art segregation measures given newly availabile point data
              * Design and implement ETL workflow using Python
                * Integrate legacy Python and R code into workflow
                * Develop metrics to evaluate data integrity/quality
                * Optimize process for scaling to 69 cities in 1930 (>30M records)
              * Use Python, Stata, and Matlab to...
                * Validate accuracy of digitized street names using additional data
                * Perform fuzzy string matching to correct street names using additional data
                * Extract Census block numbers from historic maps using machine vision
                * Report relevant metrics to assess process performance
              * Analyze residential segregation patterns in 1930 St. Louis for 10+ racial/ethnic groups
    design:
      columns: '2'
#  - block: portfolio
#    id: projects
#    content:
#      title: Projects
#      filters:
#        folders:
#          - project
#      # Default filter index (e.g. 0 corresponds to the first `filter_button` instance below).
#      default_button_index: 0
#      # Filter toolbar (optional).
#      # Add or remove as many filters (`filter_button` instances) as you like.
#      # To show all items, set `tag` to "*".
#      # To filter by a specific tag, set `tag` to an existing tag name.
#      # To remove the toolbar, delete the entire `filter_button` block.
#      buttons:
#        - name: All
#          tag: '*'
#        - name: Deep Learning
#          tag: Deep Learning
#        - name: Other
#          tag: Demo
#    design:
#      # Choose how many columns the section has. Valid values: '1' or '2'.
#      columns: '1'
#      view: showcase
#      # For Showcase view, flip alternate rows?
#      flip_alt_rows: false
#  - block: collection
#    id: publications
#    content:
#      title: Recent Publications
#      text: |-
#        {{% callout note %}}
#        Quickly discover relevant content by [filtering publications](./publication/).
#        {{% /callout %}}
#      filters:
#        folders:
#          - publication
#        exclude_featured: true
#    design:
#      columns: '2'
#      view: citation
#  - block: collection
#    id: talks
#    content:
#      title: Recent & Upcoming Talks
#      filters:
#        folders:
#          - event
#    design:
#      columns: '2'
#      view: compact
#  - block: markdown
#    content:
#      title: Gallery
#      subtitle: ''
#      text: |-
#        {{< gallery album="demo" >}}
#    design:
#      columns: '1'
---
