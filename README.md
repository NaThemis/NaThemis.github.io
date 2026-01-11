# NathalieDecode Website

A blogging site sharing discoveries and reflections around legal, data and AI topics, built with MkDocs Material.

## 🚀 Quick Start

### Prerequisites

- Python 3.11+ (currently using 3.13)
- [uv](https://docs.astral.sh/uv/) package manager

### Run

uv run mkdocs serve
Open your browser and navigate to `http://localhost:8000` to view the site.



### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd nathemiswebsite
   ```

2. **Install uv (if not already installed)**
   ```bash
   pip install uv
   ```

3. **Install dependencies**
   ```bash
   uv sync
   ```

## 🛠️ Development

### Activate Virtual Environment

```bash
# Activate the virtual environment managed by uv
uv shell
```

Alternatively, you can run commands directly with uv:
```bash
uv run <command>
```

### Local Development Server

Start the local development server to preview your site:

```bash
# With activated virtual environment
mkdocs serve

# Or directly with uv
uv run mkdocs serve
```

The site will be available at `http://localhost:8000` with auto-reload enabled.

### Building the Site

To build the static site:

```bash
# With activated virtual environment
mkdocs build

# Or directly with uv
uv run mkdocs build
```

The built site will be in the `site/` directory.

## 📝 Content Management

### Adding New Blog Posts

1. Create a new Markdown file in [`docs/posts/`](docs/posts/):
   ```markdown
   ---
   date:
       created: YYYY-MM-DD
       updated: YYYY-MM-DD
   draft: false
   authors: 
       - nathalie
       - sebastien
   categories: [AI, Data Platforms]
   readtime: 15
   slug: your-post-slug
   tags: 
       - AI
       - Data Platforms
   ---

   # Your Post Title

   Your content here...

   <!-- more -->

   Extended content after the break...
   ```

2. Available authors are defined in [`docs/.authors.yml`](docs/.authors.yml)

### Managing Authors

Edit [`docs/.authors.yml`](docs/.authors.yml) to add or modify author information:

```yaml
authors:
  username:
    name: Full Name
    description: Bio description
    avatar: URL to avatar image
    url: Personal/LinkedIn URL
```

### Customizing Styles

Modify [`docs/stylesheet/custom.css`](docs/stylesheet/custom.css) to customize the site appearance.

## 🚀 Deployment

### Automatic Deployment

The site automatically deploys to GitHub Pages when you push to the `main` branch via GitHub Actions (see [`.github/workflows/ci.yml`](.github/workflows/ci.yml)).

### Manual Deployment

```bash
# Deploy to GitHub Pages
uv run mkdocs gh-deploy --force
```

## 📂 Project Structure

```
.
├── docs/                    # Documentation source files
│   ├── .authors.yml        # Author definitions
│   ├── index.md            # Homepage
│   ├── tags.md             # Tags page
│   ├── posts/              # Blog posts
│   ├── images/             # Static images
│   └── stylesheet/         # Custom CSS
├── hooks/                   # MkDocs hooks
│   └── socialmedia.py      # Social media sharing functionality
├── overrides/               # Theme overrides
│   └── partials/
│       └── comments.html   # Giscus comments integration
├── .github/workflows/       # GitHub Actions
├── mkdocs.yml              # MkDocs configuration
├── pyproject.toml          # Python project configuration
└── main.py                 # Main Python script
```

## 🔧 Configuration

### MkDocs Configuration

The main configuration is in [`mkdocs.yml`](mkdocs.yml), including:

- **Theme**: Material Design with dark/light mode toggle
- **Plugins**: Blog, RSS, Git integration, search, tags
- **Social Links**: LinkedIn integration
- **Custom Hooks**: Social media sharing buttons

### Python Dependencies

Dependencies are managed in [`pyproject.toml`](pyproject.toml). To update dependencies:

```bash
# Update all dependencies
uv sync --upgrade

# Add a new dependency
uv add package-name

# Add a development dependency
uv add --dev package-name
```

## 🔄 Contributing Workflow

### Making Changes

1. **Create a new branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Add/edit blog posts in `docs/posts/`
   - Modify configuration if needed
   - Test locally with `uv run mkdocs serve`

3. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: your descriptive commit message"
   ```

4. **Push to your branch**
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Create a Pull Request** to merge into `main`

### Direct Updates to Main

For quick updates (like new blog posts):

1. **Ensure you're on main branch**
   ```bash
   git checkout main
   git pull origin main
   ```

2. **Make your changes and test locally**
   ```bash
   uv run mkdocs serve
   ```

3. **Commit and push**
   ```bash
   git add .
   git commit -m "Add: new blog post about [topic]"
   git push origin main
   ```

4. **Automatic deployment** will trigger via GitHub Actions

## 🔍 Features

- **Responsive Design**: Material Design theme with mobile support
- **Dark/Light Mode**: Toggle between themes
- **Blog Functionality**: Automatic post organization and RSS feed
- **Social Sharing**: Integrated X (Twitter) and Facebook sharing buttons
- **Comments**: Giscus-powered comments system
- **Search**: Full-text search across all content
- **Git Integration**: Automatic author attribution and revision dates
- **SEO Optimized**: Meta tags, sitemap, and RSS feed

## 📧 Support

For questions or issues, please check the [MkDocs Material documentation](https://squidfunk.github.io/mkdocs-material/) or open an issue in this repository.