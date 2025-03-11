import os
import glob
import markdown
import frontmatter
import re
from jinja2 import Environment, FileSystemLoader
import jinja2
from datetime import datetime
import shutil
import random

try:
    import jinja2_time
    time_extension_loaded = True
except ModuleNotFoundError:
    print("jinja2_time is not installed. Please install it with: pip install jinja2_time")
    time_extension_loaded = False

# Configure directories
CONTENT_DIR = os.path.join(os.getcwd(), "content")
OUTPUT_DIR = os.path.join(os.getcwd(), "site")
TEMPLATE_DIR = os.path.join(os.getcwd(), "templates")

def ensure_dir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def process_md(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        post = frontmatter.load(f)
    
    # Process the markdown content without replacing missing images
    html = markdown.markdown(post.content, extensions=['fenced_code', 'tables', 'toc'])
    
    post.metadata['content'] = html
    post.metadata['filename'] = os.path.splitext(os.path.basename(filepath))[0]
    return post.metadata

def render_page(template_name, context, out_filename):
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    
    # Add current year directly to context instead of using a filter
    context['current_year'] = datetime.now().year
    
    template = env.get_template(template_name)
    rendered = template.render(**context)
    
    # Ensure directory exists for the output file
    output_path = os.path.join(OUTPUT_DIR, out_filename)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(rendered)

def copy_static_files():
    """Copy static files from templates directory to the output directory"""
    # Define static files to copy
    static_files = [
        # Source files in templates or other directories
        {"src": os.path.join("templates", "script.js"), "dest": "script.js"},
        {"src": os.path.join("templates", "components.js"), "dest": "components.js"},
        {"src": os.path.join("templates", "styles.css"), "dest": "styles.css"},
    ]
    
    # Create destination directories if needed
    ensure_dir(OUTPUT_DIR)
    
    # Copy each static file
    for file_info in static_files:
        src_path = os.path.join(os.getcwd(), file_info["src"])
        dest_path = os.path.join(OUTPUT_DIR, file_info["dest"])
        
        if os.path.exists(src_path):
            print(f"Copying {src_path} to {dest_path}")
            shutil.copy(src_path, dest_path)
        else:
            print(f"Warning: Static file {src_path} not found")
            
            # If file doesn't exist in templates, use the create_default_file function
            # to create a default version in the output directory
            if file_info["dest"] == "script.js":
                create_default_file(dest_path, DEFAULT_SCRIPT_JS)
            elif file_info["dest"] == "components.js":
                create_default_file(dest_path, DEFAULT_COMPONENTS_JS)
            elif file_info["dest"] == "styles.css":
                create_default_file(dest_path, DEFAULT_STYLES_CSS)

# Default content for static files
DEFAULT_SCRIPT_JS = """// Basic JavaScript for the site
document.addEventListener('DOMContentLoaded', function() {
  console.log('Site loaded successfully!');
});"""

DEFAULT_COMPONENTS_JS = """// Component functionality for the site
function highlightCurrentPage() {
  const currentPage = window.location.pathname.split('/').pop();
  document.querySelectorAll('nav a').forEach(link => {
    if (link.getAttribute('href') === currentPage) {
      link.classList.add('active');
    }
  });
}

document.addEventListener('DOMContentLoaded', function() {
  highlightCurrentPage();
});"""

# Update the DEFAULT_STYLES_CSS to match our new styles.css file
DEFAULT_STYLES_CSS = """/* Color Variables */
:root {
  --primary-color: #4e8cca; /* Lighter blue */
  --primary-light: #6ca2d4; /* Even lighter blue */
  --primary-dark: #3a6d9a; /* Medium blue */
  --accent-purple: #9370DB; /* Medium orchid - more feminine purple */
  --accent-teal: #5ab8b8; /* Lighter teal */
  --accent-rose: #d16b80; /* Soft rose color */
  --dark-bg: #293548; /* Lighter navy background */
  --dark-bg-alt: #384862; /* Slightly lighter navy */
  --dark-content: rgba(45, 55, 75, 0.9); /* Lighter content background */
}

/* Basic Page Styling */
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Helvetica Neue', Arial, sans-serif;
  color: #fff;
  background: var(--dark-bg);
  overflow-x: hidden;
}

/* Header and Navigation */
header {
  background-color: var(--dark-bg-alt);
  padding: 1.5rem 0;
  transition: all 0.3s ease;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
  z-index: 1030;
}

nav ul {
  list-style: none;
  display: flex;
  justify-content: center;
  padding: 0;
}

nav ul li {
  margin: 0 0.5rem;
  position: relative;
}

nav ul li a {
  color: #fff;
  text-decoration: none;
  transition: all 0.3s ease;
}

nav ul li a:after {
  content: '';
  position: absolute;
  bottom: -5px;
  left: 50%;
  width: 0;
  height: 2px;
  background: var(--primary-color);
  transition: all 0.3s ease;
  transform: translateX(-50%);
}

nav ul li a:hover:after, 
nav ul li a.active:after {
  width: 100%;
}

/* Main Content */
main {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
}

article {
  margin-bottom: 2rem;
}

h1, h2, h3 {
  margin-bottom: 1rem;
}

p {
  margin-bottom: 1rem;
}

ul {
  margin-left: 1.5rem;
  margin-bottom: 1rem;
}

a {
  color: var(--primary-light);
  text-decoration: none;
}

a:hover {
  color: var(--primary-color);
}

/* Footer */
footer {
  background-color: var(--dark-bg-alt);
  color: #fff;
  text-align: center;
  padding: 1rem 0;
  margin-top: 2rem;
}

/* Project Cards */
.project-card {
  background-color: rgba(20, 20, 20, 0.9);
  color: #fff;
  border: 2px solid var(--primary-color);
  border-radius: 10px;
  margin-bottom: 2rem;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  box-shadow: 0 0 15px rgba(125, 185, 219, 0.2);
  overflow: hidden;
}

.project-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(125, 185, 219, 0.3);
}

/* Blog Tags */
.tag {
  background-color: var(--primary-dark);
  padding: 0.2rem 0.5rem;
  border-radius: 3px;
  margin-right: 0.5rem;
  color: #fff;
  font-size: 0.85rem;
}

/* Responsive Styles */
@media (max-width: 768px) {
  nav ul {
    flex-direction: column;
    align-items: center;
  }
  
  nav ul li {
    margin: 0.5rem 0;
  }
}
"""

def create_default_file(filepath, content):
    """Create a default file with the specified content"""
    print(f"Creating default file: {filepath}")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def build_blogs():
    """Build individual blog posts"""
    blogs = []
    blog_dir = os.path.join(CONTENT_DIR, "blog")
    if os.path.exists(blog_dir):
        # Output blog posts directly to the main site directory
        for md_file in glob.glob(os.path.join(blog_dir, "*.md")):
            blog = process_md(md_file)
            blogs.append(blog)
            # Changed to output directly to site root
            render_page("blog-post.html", {"blog": blog}, f"{blog['filename']}.html")
    
    # Sort blogs by date if available
    blogs.sort(key=lambda x: x.get("date", ""), reverse=True)
    return blogs

def build_index(projects, about_content):
    context = {
        "projects": projects,
        "about": about_content
    }
    render_page("index.html", context, "index.html")

def build_portfolio(projects):
    context = {"projects": projects}
    render_page("portfolio.html", context, "portfolio.html")

def build_projects():
    projects = []
    for md_file in glob.glob(os.path.join(CONTENT_DIR, "projects", "*.md")):
        projects.append(process_md(md_file))
    # Optional: sort projects based on an 'order' key
    projects.sort(key=lambda x: x.get("order", 999))
    for proj in projects:
        render_page("project.html", {"project": proj}, f"{proj['filename']}.html")
    return projects

def build_page(page_name):
    # Build a simple page (about, resume, blog etc.) from content/pages
    filepath = os.path.join(CONTENT_DIR, "pages", f"{page_name}.md")
    if not os.path.exists(filepath):
        print(f"Warning: Content file {filepath} not found. Creating placeholder.")
        ensure_dir(os.path.dirname(filepath))
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"""---
title: {page_name.title()}
subtitle: {page_name.title()} Page
---
# {page_name.title()}

This is a placeholder for the {page_name} page. Please update this content.
""")
    page = process_md(filepath)
    render_page("page.html", {"page": page}, f"{page_name}.html")
    return page

# Update the frontmatter parsing to include new fields
def parse_frontmatter(content):
    frontmatter = {}
    # Standard fields
    frontmatter['title'] = extract_field(frontmatter_text, 'title')
    frontmatter['subtitle'] = extract_field(frontmatter_text, 'subtitle')
    frontmatter['description'] = extract_field(frontmatter_text, 'description')
    frontmatter['excerpt'] = extract_field(frontmatter_text, 'excerpt')
    frontmatter['technologies'] = extract_list_field(frontmatter_text, 'technologies')
    frontmatter['order'] = extract_field(frontmatter_text, 'order', default=999)
    frontmatter['image'] = extract_field(frontmatter_text, 'image', default='')
    frontmatter['github'] = extract_field(frontmatter_text, 'github', default='')
    frontmatter['demo'] = extract_field(frontmatter_text, 'demo', default='')
    return frontmatter, content

# Update the HTML generation to handle the new image and gallery elements
def generate_project_html(project):
    html = ""
    # Handle project main image
    if project.get('image'):
        html += f'<div class="project-main-image"><img src="{project["image"]}" alt="{project["title"]}" /></div>\n'
    
    # Handle HTML content that may include gallery and controlled images
    html += process_html_content(project['content'])
    
    return html

# Add a function to process HTML content
def process_html_content(content):
    # This function will ensure HTML elements like galleries are properly handled
    # You might need a more sophisticated approach if you're using a markdown parser
    processed_content = content
    
    # Handle any special transformations needed for HTML elements
    # For example, you might need to add CSS classes to gallery elements
    
    return processed_content

# Update the CSS generation to include styles for project images and galleries
def generate_css():
    css = """
    .project-image {
      width: 100%;
      height: auto;
      border-radius: 8px;
      margin: 20px 0;
    }
    
    .project-gallery {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
      grid-gap: 16px;
      margin: 30px 0;
    }
    
    .gallery-card {
      width: 100%;
      height: 180px;
      object-fit: cover;
      border-radius: 6px;
      transition: transform 0.3s ease;
    }
    
    .gallery-card:hover {
      transform: scale(1.03);
    }
    """
    return css

# Make sure to rebuild all project files
def rebuild_all():
    # Clear any caches
    if hasattr(rebuild_all, 'cache'):
        delattr(rebuild_all, 'cache')
    
    # Force rebuild of all files

def main():
    ensure_dir(OUTPUT_DIR)
    # Copy static files
    copy_static_files()
    # Build projects from content/projects
    projects = build_projects()
    # Build blog posts
    blogs = build_blogs()
    
    # Extract categories and tags for indexing
    categories = {}
    tags = {}
    for blog in blogs:
        # Index categories
        category = blog.get('category')
        if category:
            if category in categories:
                categories[category] += 1
            else:
                categories[category] = 1
        
        # Index tags
        blog_tags = blog.get('tags', [])
        for tag in blog_tags:
            if tag in tags:
                tags[tag] += 1
            else:
                tags[tag] = 1
    
    # Build standard pages from content/pages (expecting about, resume, blog)
    about = build_page("about")
    resume = build_page("resume")
    
    # Build blog page with list of blog posts
    blog_page = build_page("blog")
    render_page("blog.html", {
        "page": blog_page, 
        "blogs": blogs,
        "categories": categories,
        "tags": tags
    }, "blog.html")
    
    # Build index with portfolio projects and about excerpt
    build_index(projects, about)
    # Build portfolio page which lists all projects
    build_portfolio(projects)
    
    # Create assets directory for downloadable files
    assets_dir = os.path.join(OUTPUT_DIR, "assets")
    ensure_dir(assets_dir)
    
    # Create a placeholder resume PDF if it doesn't exist
    resume_pdf_path = os.path.join(assets_dir, "Chloe_Walsh_Resume.pdf")
    if not os.path.exists(resume_pdf_path):
        # If we had a real PDF we would copy it, but for now create a placeholder file
        with open(resume_pdf_path, 'wb') as f:
            f.write(b'%PDF-1.5\n%Placeholder resume file')
    
    print("Site build complete.")

if __name__ == "__main__":
    main()
