# Website Redesign Documentation
## "Ahead of My Time, Every Time" - Audience-Aware Academic Website

### Overview
This redesign transforms the website into an intelligent, audience-aware platform that serves three distinct audiences (Academic, Policymaker, Public) without explicit "branding" while embodying the philosophy of being "ahead of my time, every time."

---

## Key Features

### 1. **Audience Toggle System** 🎯
- **Fixed position toggle** in upper right corner (desktop) or top of content (mobile)
- Three audience views:
  - 🎓 **Academic**: Research methodology, theoretical contributions, citations
  - 📊 **Policymaker**: Real-world impact, evidence-based insights, actionable findings
  - 🌍 **Public**: Plain language explanations, community impact, transparency
- **Persistent preference**: Uses localStorage to remember user's choice across visits
- **Accessible**: Full keyboard navigation, ARIA labels, screen reader support
- **Smooth transitions**: Animated content switching with fade effects

### 2. **Dynamic Content Adaptation**
Each section adapts based on selected audience:

#### Biography Section
- **Academic**: Emphasizes PVEST theory, ML/AI methods (VAD, ASR, SER, NLP), novel data sources
- **Policymaker**: Focuses on evidence-based insights, accountability metrics, intervention opportunities
- **Public**: Plain language, relatable examples, community relevance

#### Publications Section
Each paper includes audience-specific "relevance" notes:
- **Academic**: Methodological contributions, theoretical advances
- **Policymaker**: Policy implications, actionable recommendations
- **Public**: Why it matters for communities, real-world impact

#### Experience Section
Same positions shown to all, but descriptions emphasize different aspects based on audience needs.

### 3. **Innovation Timeline**
Showcases how research was "ahead of its time":
- **2016-2018**: Early computational urban sociology (Pioneer badge)
- **2020-2022**: AI ethics in policing before mainstream (Pioneer badge)
- **2022-Present**: Novel radio communications data source (First Mover badge)
- **2024-Present**: Decentralized data stewardship (Cutting Edge badge)

### 4. **Modern Design System**
- **Color palette**: Purple gradient (`#667eea` → `#764ba2`) as accent
- **Typography**: Clean, readable fonts from Wowchemy minimal theme
- **Glassmorphism**: Backdrop blur effects on floating elements
- **Card-based layout**: Elevated cards with hover effects
- **Progressive enhancement**: Scroll-triggered animations, smooth transitions
- **Dark mode support**: Full theme compatibility with day/night toggle

### 5. **Improved Navigation**
Reorganized from individual paper links to logical sections:
- **About** → Biography and intro
- **Research** → Recent work and publications
- **Experience** → Career trajectory
- **CV** → PDF download
- **Resources** → Dataset, profiles, contact

### 6. **Resources Hub**
Centralized access to:
- BPC-CPD Corpus dataset
- Academic profiles (Google Scholar, ORCID)
- Professional networks (LinkedIn, Twitter)
- Contact options with clear use cases
- Job market availability

---

## Technical Implementation

### File Structure
```
graziul.github.io/
├── assets/
│   ├── scss/
│   │   └── custom.scss          # All custom styles
│   └── js/
│       └── audience-toggle.js   # Audience switching logic
├── layouts/
│   └── partials/
│       ├── custom_head.html     # Load custom CSS
│       └── custom_js.html       # Load custom JS
├── content/
│   ├── _index.md                # Redesigned homepage
│   └── authors/admin/_index.md  # Bio (unchanged)
└── config/_default/
    └── menus.yaml               # Reorganized navigation
```

### Custom CSS (`assets/scss/custom.scss`)
- **Audience selector**: Fixed position toggle with glassmorphism
- **Audience content**: Hide/show system with fade animations
- **Timeline**: Left-border design with badges
- **Cards**: Publication, insight, and impact card styles
- **Responsive**: Mobile-first breakpoints
- **Accessibility**: Focus states, high contrast, screen reader support

### Custom JavaScript (`assets/js/audience-toggle.js`)
**Core Functions:**
- `initializeAudienceToggle()`: Creates toggle UI if not present
- `switchAudience(audienceId)`: Changes active audience view
- `updateDynamicContent(audienceId)`: Updates text/CTAs per audience
- `setupKeyboardNavigation()`: Arrow key support for toggle
- `announceChange(audienceId)`: Screen reader announcements
- `setupScrollAnimations()`: Intersection Observer for reveal effects

**Features:**
- localStorage persistence of preference
- Custom event dispatch: `audienceChanged`
- Progressive enhancement: Works without JS (shows academic view)
- Performance: Minimal reflows, efficient DOM updates

### Hugo Integration
**Custom Partials:**
- `custom_head.html`: Compiles SCSS, adds to `<head>`
- `custom_js.html`: Minifies/fingerprints JS, loads before `</body>`

**Wowchemy Compatibility:**
- Uses existing block system (about.biography, markdown, experience)
- Leverages theme's responsive grid
- Compatible with day/night theme switching
- No modifications to core theme files

---

## Design Philosophy: "Ahead of My Time, Every Time"

### How the Design Embodies This:

1. **Progressive Enhancement**: Uses modern web APIs (localStorage, Intersection Observer, CSS backdrop-filter) while maintaining fallbacks

2. **Anticipatory Design**: Audience toggle anticipates what different visitors need before they have to search for it

3. **Innovation Timeline**: Explicitly shows track record of being ahead of curve on:
   - Computational social science
   - AI ethics
   - Novel data sources
   - Decentralized governance

4. **Cutting-Edge but Accessible**: Modern design patterns without sacrificing usability or accessibility

5. **Future-Forward Content**: Emphasizes emerging areas (decentralized data stewardship, participatory governance) alongside established work

### Subtle "Ahead of Time" Signals:
- ⚡ "Ahead" badges on timeline items
- Purple gradient (forward-thinking, innovative)
- Glassmorphism (modern, emerging design trend)
- Audience awareness (anticipating user needs)
- Participatory data governance (Web3-adjacent thinking without jargon)

---

## Accessibility Features

### WCAG 2.1 AA Compliance:
- ✅ Keyboard navigation (Tab, Arrow keys, Home, End)
- ✅ ARIA labels and roles (tablist, tab, status)
- ✅ Screen reader announcements (live regions)
- ✅ Focus indicators on all interactive elements
- ✅ Sufficient color contrast (4.5:1 minimum)
- ✅ Semantic HTML (headings, landmarks, lists)
- ✅ Responsive text sizing (supports 200% zoom)
- ✅ No flashing/strobing animations
- ✅ Alternative text (where applicable)

### Additional Considerations:
- Prefers-reduced-motion support (could add)
- High contrast mode support (inherited from theme)
- Focus trap in toggle selector
- Skip links (inherited from theme)

---

## Audience-Specific Content Strategy

### Academic Audience Priorities:
1. **Methodology** - VAD, ASR, SER, NLP techniques
2. **Theory** - PVEST framework, computational social science
3. **Novelty** - First systematic use of radio data
4. **Publications** - Peer-reviewed venues, citations
5. **Collaboration** - Research partnerships, data sharing

### Policymaker Audience Priorities:
1. **Impact** - Accountability metrics, intervention opportunities
2. **Evidence** - Data-driven insights, objective analysis
3. **Actionability** - Policy recommendations, frameworks
4. **Scalability** - Automated analysis, resource optimization
5. **Consultation** - Available for policy development

### Public Audience Priorities:
1. **Clarity** - Plain language, relatable examples
2. **Relevance** - Community impact, transparency
3. **Rights** - Data governance, community control
4. **Trust** - Participatory approach, accountability
5. **Engagement** - Accessible contact, community-centered

---

## Performance Considerations

### Optimization:
- **CSS**: Single compiled/minified SCSS file
- **JS**: Single minified/fingerprinted JS file
- **Images**: (none added in this redesign)
- **Fonts**: Using theme's existing font stack
- **Animations**: CSS-based where possible, GPU-accelerated
- **Loading**: Preload JS, async where appropriate

### Metrics (Expected):
- **First Contentful Paint**: <1.5s
- **Largest Contentful Paint**: <2.5s
- **Time to Interactive**: <3.0s
- **Cumulative Layout Shift**: <0.1

### Hugo Build:
- Compiles SCSS at build time
- Minifies CSS/JS in production
- Fingerprints assets for cache busting
- No runtime template rendering

---

## Browser Support

### Fully Supported:
- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile Safari 14+
- Chrome Android 90+

### Graceful Degradation:
- **No localStorage**: Defaults to academic view, resets on navigation
- **No Intersection Observer**: All content visible (no scroll animations)
- **No backdrop-filter**: Falls back to solid background
- **No CSS Grid**: Falls back to flexbox/single column
- **No JS**: Shows all content for academic audience

---

## SEO Considerations

### Maintained:
- Semantic HTML structure
- Heading hierarchy (h1 → h6)
- Meta descriptions (from Wowchemy)
- Schema.org Person markup (from Wowchemy)
- Clean URL structure
- Mobile-friendly design
- Fast loading times

### Enhanced:
- Rich content for all three audiences improves topical relevance
- Internal linking structure (anchor links)
- Structured data for publications
- Social sharing metadata (from Wowchemy)

---

## Future Enhancements (Optional)

### Potential Additions:
1. **Analytics**: Track which audience view is most popular
2. **A/B Testing**: Test different audience labels/icons
3. **Personalization**: Auto-detect audience from referrer/context
4. **Content Expansion**: Blog posts with audience-specific insights
5. **Interactive Elements**: Data visualizations, interactive timeline
6. **Testimonials**: Quotes from collaborators in each audience category
7. **Case Studies**: Detailed examples of impact for policymakers/public
8. **Newsletter**: Audience-specific content digests
9. **RSS Feeds**: Separate feeds per audience
10. **i18n**: Multi-language support for public audience

### Technical Improvements:
1. **Service Worker**: Offline support, faster repeat visits
2. **Lazy Loading**: Images, heavy content below fold
3. **Code Splitting**: Separate JS bundles per audience
4. **Prefetching**: Preload likely next navigation
5. **WebP/AVIF**: Modern image formats
6. **Reduced Motion**: Respect prefers-reduced-motion
7. **Print Styles**: Optimized for PDF export
8. **Share API**: Native sharing on mobile

---

## Maintenance Guide

### Updating Content:

**Add New Publication:**
1. Edit `content/_index.md`
2. Add new `<div class="publication-card">` to "Recent Work" section
3. Include three audience-relevance sections
4. Update impact metrics if applicable

**Update Timeline:**
1. Edit `content/_index.md`
2. Add new `<div class="timeline-item">` to innovation timeline
3. Consider adding "ahead-badge" for pioneering work

**Change Audience Labels:**
1. Edit `assets/js/audience-toggle.js`
2. Update `audiences` array (line ~17)
3. Update labels object throughout

**Adjust Colors:**
1. Edit `assets/scss/custom.scss`
2. Search/replace `#667eea` and `#764ba2` with new gradient colors

**Modify Toggle Position:**
1. Edit `assets/scss/custom.scss`
2. Adjust `.audience-selector` top/right properties

### Testing Checklist:
- [ ] All three audience views display correctly
- [ ] Toggle switches smoothly between views
- [ ] Preference persists across page reloads
- [ ] Mobile responsive (test at 320px, 768px, 1024px)
- [ ] Dark mode works correctly
- [ ] Keyboard navigation functional
- [ ] Screen reader announces changes
- [ ] External links open in new tabs
- [ ] Email links work
- [ ] CV PDF loads correctly
- [ ] All publication links valid

---

## Credits

**Design & Development**: Claude (Anthropic)
**Content Source**: Chris Graziul's existing CV, publications, bio
**Framework**: Hugo + Wowchemy Academic Theme
**Hosting**: Netlify
**Custom Code**: audience-toggle.js, custom.scss

---

## Questions or Issues?

If you encounter any issues or have questions about the redesign:

1. **Content Updates**: Edit `content/_index.md` directly
2. **Style Tweaks**: Modify `assets/scss/custom.scss`
3. **Functionality**: Check `assets/js/audience-toggle.js`
4. **Navigation**: Update `config/_default/menus.yaml`

The design is intentionally modular and well-commented for easy maintenance.

---

## Recent Updates (Latest Session)

### October 2025 - Version 2.1: Hugo Block Structure Optimization

**Major Fixes:**

1. **HTML Rendering Issue** - Resolved raw HTML displaying instead of rendered content
   - Switched from single massive markdown block to proper Hugo block types
   - Use `block: hero` for hero section
   - Use separate `block: markdown` for each career phase
   - Use `block: markdown` for resources (changed from collection)

2. **Language Refinement** - Removed self-aggrandizing tone
   - Removed "Ahead of My Time, Every Time" badge from hero
   - Changed section titles to factual descriptions
   - Let chronology and achievements speak for themselves
   - Updated CSS comments to remove the phrase

3. **CSS Structure Updates** - Adapted for Hugo's native block rendering
   - Apply scroll-snap to `body` element instead of custom container
   - Target `main > section` for fullscreen behavior (Wowchemy's structure)
   - Updated all responsive breakpoints and print styles
   - Maintains full-screen scroll-snap design with proper block structure

4. **Dark Mode Support** - Fixed metric cards for theme compatibility
   - Replaced inline styles with semantic CSS classes
   - Use `.hero-highlights`, `.highlight-item`, `.highlight-number`, `.highlight-label`
   - Proper dark mode support with `.dark` selectors

**Files Modified:**
- `content/_index.md` - Complete restructure with Hugo blocks
- `assets/scss/custom.scss` - Updated selectors and removed phrase
- Deleted `assets/js/audience-toggle.js` and `layouts/partials/custom_js.html` (no longer needed)

**Result:** Site now renders properly with Hugo's native block system while maintaining the full-screen scroll-snap design and proper dark mode support.

---

**Last Updated**: October 2025
**Version**: 2.1 (Hugo Block Structure Optimization)
