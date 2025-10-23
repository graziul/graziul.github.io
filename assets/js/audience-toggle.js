/**
 * Audience Toggle Functionality
 * Enables switching between Academic, Policymaker, and Public views
 * "Ahead of my time, every time" - Progressive enhancement
 */

(function() {
  'use strict';

  // Initialize audience preference from localStorage or default to 'academic'
  let currentAudience = localStorage.getItem('audience-preference') || 'academic';

  // Initialize on page load
  document.addEventListener('DOMContentLoaded', function() {
    initializeAudienceToggle();
    switchAudience(currentAudience, false); // Don't animate on initial load
  });

  function initializeAudienceToggle() {
    // Create the audience selector if it doesn't exist
    let selector = document.querySelector('.audience-selector');

    if (!selector) {
      // Create selector dynamically
      selector = document.createElement('div');
      selector.className = 'audience-selector';
      selector.setAttribute('role', 'tablist');
      selector.setAttribute('aria-label', 'Select audience view');

      const audiences = [
        { id: 'academic', label: 'Academic', icon: '🎓' },
        { id: 'policymaker', label: 'Policymaker', icon: '📊' },
        { id: 'public', label: 'Public', icon: '🌍' }
      ];

      audiences.forEach(audience => {
        const btn = document.createElement('button');
        btn.className = 'audience-btn';
        btn.setAttribute('data-audience', audience.id);
        btn.setAttribute('role', 'tab');
        btn.setAttribute('aria-selected', audience.id === currentAudience ? 'true' : 'false');
        btn.setAttribute('aria-controls', `${audience.id}-content`);
        btn.textContent = `${audience.icon} ${audience.label}`;

        btn.addEventListener('click', function() {
          switchAudience(audience.id);
        });

        selector.appendChild(btn);
      });

      // Insert after navbar or at top of main content
      const navbar = document.querySelector('.navbar');
      if (navbar) {
        navbar.parentNode.insertBefore(selector, navbar.nextSibling);
      } else {
        document.body.insertBefore(selector, document.body.firstChild);
      }
    }

    // Set up keyboard navigation
    setupKeyboardNavigation();
  }

  function switchAudience(audienceId, animate = true) {
    currentAudience = audienceId;

    // Save preference
    localStorage.setItem('audience-preference', audienceId);

    // Update button states
    const buttons = document.querySelectorAll('.audience-btn');
    buttons.forEach(btn => {
      const isActive = btn.getAttribute('data-audience') === audienceId;
      btn.classList.toggle('active', isActive);
      btn.setAttribute('aria-selected', isActive ? 'true' : 'false');
    });

    // Show/hide content sections
    const contentSections = document.querySelectorAll('.audience-content');
    contentSections.forEach(section => {
      const isRelevant = section.getAttribute('data-audience') === audienceId;

      if (animate) {
        section.classList.add('loading');
        setTimeout(() => {
          section.classList.toggle('active', isRelevant);
          section.classList.remove('loading');
          section.setAttribute('aria-hidden', !isRelevant);
        }, 150);
      } else {
        section.classList.toggle('active', isRelevant);
        section.setAttribute('aria-hidden', !isRelevant);
      }
    });

    // Update dynamic content
    updateDynamicContent(audienceId);

    // Announce change to screen readers
    announceChange(audienceId);

    // Trigger custom event for other scripts
    document.dispatchEvent(new CustomEvent('audienceChanged', {
      detail: { audience: audienceId }
    }));

    // Smooth scroll to top of main content
    if (animate) {
      const mainContent = document.querySelector('.audience-content.active');
      if (mainContent) {
        mainContent.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
    }
  }

  function updateDynamicContent(audienceId) {
    // Update bio text if it exists
    const bioText = document.querySelector('.bio-dynamic-text');
    if (bioText) {
      const texts = {
        academic: 'My research examines the promise and limits of AI/ML-based tools to study policing, specifically how two-way radio use relates to officer coordination and behavior.',
        policymaker: 'I develop evidence-based tools and frameworks to help policymakers understand police behavior through innovative analysis of radio communications data.',
        public: 'I use artificial intelligence to study how police communicate and coordinate, helping communities better understand policing in their neighborhoods.'
      };
      bioText.textContent = texts[audienceId];
    }

    // Update CTAs
    const ctas = document.querySelectorAll('.cta-audience-specific');
    ctas.forEach(cta => {
      const ctaTexts = {
        academic: 'View Publications',
        policymaker: 'See Policy Insights',
        public: 'Learn More'
      };
      const audienceText = cta.getAttribute(`data-${audienceId}-text`);
      if (audienceText) {
        cta.textContent = audienceText;
      } else if (ctaTexts[audienceId]) {
        cta.textContent = ctaTexts[audienceId];
      }
    });

    // Update experience descriptions to focus on different aspects
    updateExperienceDescriptions(audienceId);
  }

  function updateExperienceDescriptions(audienceId) {
    const experienceCards = document.querySelectorAll('.experience-card');
    experienceCards.forEach(card => {
      const academicDesc = card.querySelector('.desc-academic');
      const policymakerDesc = card.querySelector('.desc-policymaker');
      const publicDesc = card.querySelector('.desc-public');

      if (academicDesc) academicDesc.style.display = audienceId === 'academic' ? 'block' : 'none';
      if (policymakerDesc) policymakerDesc.style.display = audienceId === 'policymaker' ? 'block' : 'none';
      if (publicDesc) publicDesc.style.display = audienceId === 'public' ? 'block' : 'none';
    });
  }

  function setupKeyboardNavigation() {
    const selector = document.querySelector('.audience-selector');
    if (!selector) return;

    const buttons = selector.querySelectorAll('.audience-btn');

    buttons.forEach((button, index) => {
      button.addEventListener('keydown', function(e) {
        let targetIndex;

        switch(e.key) {
          case 'ArrowLeft':
            targetIndex = index > 0 ? index - 1 : buttons.length - 1;
            buttons[targetIndex].focus();
            e.preventDefault();
            break;
          case 'ArrowRight':
            targetIndex = index < buttons.length - 1 ? index + 1 : 0;
            buttons[targetIndex].focus();
            e.preventDefault();
            break;
          case 'Home':
            buttons[0].focus();
            e.preventDefault();
            break;
          case 'End':
            buttons[buttons.length - 1].focus();
            e.preventDefault();
            break;
        }
      });
    });
  }

  function announceChange(audienceId) {
    // Create or update live region for screen reader announcements
    let liveRegion = document.getElementById('audience-announcement');

    if (!liveRegion) {
      liveRegion = document.createElement('div');
      liveRegion.id = 'audience-announcement';
      liveRegion.setAttribute('role', 'status');
      liveRegion.setAttribute('aria-live', 'polite');
      liveRegion.style.position = 'absolute';
      liveRegion.style.left = '-10000px';
      liveRegion.style.width = '1px';
      liveRegion.style.height = '1px';
      liveRegion.style.overflow = 'hidden';
      document.body.appendChild(liveRegion);
    }

    const labels = {
      academic: 'Academic view',
      policymaker: 'Policymaker view',
      public: 'Public view'
    };

    liveRegion.textContent = `Switched to ${labels[audienceId]}`;
  }

  // Expose function globally for potential external use
  window.switchAudience = switchAudience;
  window.getCurrentAudience = () => currentAudience;

  // Add smooth reveal animation for content as user scrolls
  function setupScrollAnimations() {
    const observerOptions = {
      root: null,
      threshold: 0.1,
      rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateY(0)';
        }
      });
    }, observerOptions);

    // Observe cards and sections
    const animatedElements = document.querySelectorAll('.insight-card, .publication-card, .impact-card, .timeline-item');
    animatedElements.forEach(el => {
      el.style.opacity = '0';
      el.style.transform = 'translateY(20px)';
      el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
      observer.observe(el);
    });
  }

  // Run scroll animations after DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', setupScrollAnimations);
  } else {
    setupScrollAnimations();
  }

})();
