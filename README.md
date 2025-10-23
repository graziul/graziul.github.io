# Christopher Graziul Academic Website

Professional academic website built with [Hugo](https://gohugo.io/) and [Wowchemy](https://wowchemy.com/).

## Adding Visual Content to Your Site

This guide explains how to add images, screenshots, and other visual content to enhance your academic website.

### Image Storage Location

All images should be stored in:
```
static/uploads/images/
```

Create this directory if it doesn't exist:
```bash
mkdir -p static/uploads/images
```

### Supported Image Formats

- **Publications/Projects**: PNG, JPG, WebP (recommended for web)
- **Screenshots**: PNG (for crisp text and UI elements)
- **Photos**: JPG (for photographs)
- **Diagrams/Figures**: SVG (scalable), PNG (raster)

### Image Optimization

Before uploading images, optimize them for web:

1. **Resize** images to appropriate dimensions:
   - Full-width images: Max 1200px wide
   - Side-by-side layouts: Max 600px wide
   - Thumbnails: Max 300px wide

2. **Compress** images:
   ```bash
   # Using ImageMagick
   convert input.png -quality 85 -strip output.jpg

   # Using cwebp for WebP format
   cwebp -q 85 input.png -o output.webp
   ```

3. **Use appropriate formats**:
   - **WebP** for best compression (modern browsers)
   - **PNG** for screenshots with text
   - **JPG** for photographs

### Adding Images to Content

#### Method 1: Inline Images (Simple)

Add images directly in your markdown content:

```markdown
![Image Description](/uploads/images/my-image.jpg)
```

#### Method 2: Images with Captions

Use the custom CSS classes for styled images with captions:

```markdown
<img src="/uploads/images/my-image.jpg" alt="Description" class="item-image">
<p class="item-image-caption">Figure 1: Description of the image</p>
```

#### Method 3: Side-by-Side Layout

Use the `item-with-image` class for text alongside an image:

```markdown
<div class="item-with-image">
  <div class="item-content">
    <p>Your text content here...</p>
  </div>
  <div class="item-image-container">
    <img src="/uploads/images/my-image.jpg" alt="Description" class="item-image">
  </div>
</div>
```

### Adding Images to Specific Content Types

#### Major Publications

```markdown
<div class="item-major">
  <div class="item-title"><a href="https://doi.org/...">Publication Title</a></div>
  <div class="item-meta">Citation information...</div>

  <!-- Add image here -->
  <img src="/uploads/images/publication-figure.png" alt="Key figure from paper" class="item-image">
  <p class="item-image-caption">Figure 1: Main result showing...</p>

  <div class="item-description">
    <p>Publication description...</p>
  </div>
</div>
```

#### Datasets

```markdown
<div class="item-dataset">
  <div class="item-title"><a href="...">Dataset Name</a></div>
  <div class="item-meta">Dataset information...</div>

  <!-- Add visualization here -->
  <img src="/uploads/images/dataset-visualization.png" alt="Dataset statistics" class="item-image">

  <div class="item-description">
    <p>Dataset description...</p>
  </div>
</div>
```

#### Grants (Visual Workflow/Timeline)

```markdown
<div class="item-grant">
  <div class="item-title">Grant Title</div>
  <div class="item-meta">Funding information...</div>

  <!-- Add research workflow diagram -->
  <img src="/uploads/images/research-workflow.svg" alt="Research methodology workflow" class="item-image">

  <p>Grant description...</p>
</div>
```

### Example: Adding Images to the BPC-CPD Corpus

1. **Prepare your images**:
   - `bpc-cpd-waveform.png` - Audio waveform example
   - `bpc-cpd-statistics.png` - Corpus statistics chart
   - `bpc-cpd-pipeline.svg` - Processing pipeline diagram

2. **Upload to** `/static/uploads/images/`

3. **Update content** in `content/_index.md`:

```markdown
<div class="item-dataset">
  <div class="item-title"><a href="https://ieeexplore.ieee.org/document/10832157">Speech Recognition for Analysis of Police Radio Communication</a></div>
  <div class="item-meta">...</div>

  <img src="/uploads/images/bpc-cpd-waveform.png" alt="Example waveform from CPD radio" class="item-image">
  <p class="item-image-caption">Sample waveform from CPD dispatch zone 1</p>

  <div class="item-description">
    <p><strong>BPC-CPD Corpus:</strong> 62,080 utterances...</p>
  </div>
</div>
```

### Automated Image Generation from Data

You can generate visualizations programmatically:

#### Python Example: Generate Publication Timeline

```python
import matplotlib.pyplot as plt
import pandas as pd

# Publication data
pubs = pd.DataFrame({
    'year': [2008, 2012, 2016, 2018, 2023, 2024, 2025],
    'count': [1, 2, 1, 1, 1, 2, 1],
    'type': ['Review', 'Journal', 'Dissertation', 'Journal', 'Journal', 'Conference', 'Conference']
})

# Create visualization
fig, ax = plt.subplots(figsize=(10, 4))
ax.scatter(pubs['year'], pubs['count'], s=100, alpha=0.6, c='#6366f1')
ax.set_xlabel('Year')
ax.set_ylabel('Publications')
ax.set_title('Publication Timeline')
plt.tight_layout()
plt.savefig('static/uploads/images/publication-timeline.png', dpi=150, bbox_inches='tight')
```

#### R Example: Generate Citation Network

```r
library(ggplot2)
library(dplyr)

# Citation data
citations <- data.frame(
  year = c(2008, 2012, 2016, 2018, 2023, 2024),
  citations = c(50, 120, 200, 350, 80, 30)
)

# Create plot
ggplot(citations, aes(x=year, y=citations)) +
  geom_line(color='#6366f1', size=1.2) +
  geom_point(color='#6366f1', size=3) +
  theme_minimal() +
  labs(title='Citation Growth Over Time', x='Year', y='Citations')

ggsave('static/uploads/images/citation-growth.png', width=8, height=4, dpi=150)
```

### Screenshots from Publications

To extract figures from your publications:

1. **From PDFs**:
   ```bash
   # Extract page 3 as image
   pdftoppm -png -f 3 -l 3 -r 300 input.pdf output
   ```

2. **Crop to specific figure**:
   ```bash
   convert output-3.png -crop 800x600+100+200 figure.png
   ```

3. **Clean up and optimize**:
   ```bash
   convert figure.png -trim -quality 90 final-figure.png
   ```

### Testing Images Locally

Before deploying:

1. Start local Hugo server:
   ```bash
   hugo server -D
   ```

2. Navigate to `http://localhost:1313`

3. Check that:
   - Images load correctly
   - Images are responsive on mobile
   - Captions are properly styled
   - Links work

### Common Image Placement Locations

#### In Hero Section
```markdown
# Hero Section
- block: hero
  id: hero
  content:
    title: Christopher M. Graziul, PhD
    image: uploads/images/hero-background.jpg  # Background image
```

#### In Timeline Sections
Add images between text blocks in any timeline section (foundation, computational, policing, current).

#### In Resources Section
Add visual previews to resource cards:

```markdown
<div class="resource-card">
  <h3>BPC-CPD Corpus</h3>
  <img src="/uploads/images/corpus-preview.png" alt="Corpus preview" style="width:100%; margin:10px 0;">
  <p>Dataset description...</p>
</div>
```

### Troubleshooting

**Images not showing:**
- Check file path (should be `/uploads/images/filename.ext`)
- Verify file is in `static/uploads/images/`
- Check file permissions: `chmod 644 static/uploads/images/*.png`

**Images too large:**
- Resize before uploading
- Use WebP format for better compression
- Consider using `loading="lazy"` attribute

**Images not responsive:**
- Add `class="item-image"` to use responsive styling
- Or add inline style: `style="max-width:100%; height:auto;"`

## Site Structure

```
content/
  _index.md           # Main homepage content
config/
  _default/
    config.yaml       # Site configuration
    menus.yaml        # Navigation menu
assets/
  scss/
    custom.scss       # Custom styling
static/
  uploads/
    images/           # Image directory
    *.pdf             # CV and other documents
```

## Local Development

```bash
# Install Hugo (if not already installed)
# macOS:
brew install hugo

# Linux:
snap install hugo

# Start development server
hugo server -D

# Build for production
hugo --minify
```

## Deployment

The site automatically deploys to GitHub Pages when changes are pushed to the `master` branch via GitHub Actions (`.github/workflows/hugo.yml`).

## Citation Format

This site uses **Chicago Manual of Style** (author-date) for citations:

```
Author Last, First. "Article Title." Journal Name Volume, no. Issue (Year): Pages. DOI/URL.
```

## Visual Hierarchy

Content uses different CSS classes for visual importance:

- `.item-major` - Major publications, breakthrough work
- `.item-grant` - Grants, significant funding
- `.item-dataset` - Datasets, corpus releases
- `.item-standard` - Standard entries (degrees, positions, presentations)

## Support

For Hugo/Wowchemy documentation:
- Hugo: https://gohugo.io/documentation/
- Wowchemy: https://wowchemy.com/docs/

## License

Content © Christopher Graziul. All rights reserved.
