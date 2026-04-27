# Design System & Styling Rules

## 1. Design Principles
- **Modern & Clean**: Prioritize whitespace, generous padding, and clear typographic hierarchy.
- **Glassmorphism & Soft UI**: Use subtle shadows (`box-shadow`), rounded corners, and frosted glass effects (`backdrop-filter: blur()`) to create depth.
- **Aesthetics First**: The UI must look premium. Avoid plain HTML defaults.
- **Semantic Consistency**: Buttons should look like buttons, links like links, and interactive elements must have clear `:hover` states.

## 2. Color Theme
The color palette is centrally managed in `frontend/src/index.css`. All new components must use these variables instead of hardcoding hex values.

- **Primary Brand Color**: `--color-primary` (Vibrant Orange `#f28b46`)
  - Used for primary CTA buttons, important links, and active states.
  - Hover state: `--color-primary-hover` (`#e07730`)
- **Backgrounds**:
  - `--color-bg-main`: White (`#ffffff`) for the main application body.
  - `--color-bg-surface`: White (`#ffffff`) for cards floating above the main background.
  - `--color-bg-muted`: Very light gray (`#f9fafb`) to separate sections or provide subtle contrast.
  - `--color-bg-outer`: Soft Lavender (`#f0ecfc`) used for presentation contexts or external wrappers.
- **Text Colors**:
  - `--color-text-primary`: Dark Gray (`#1f2937`) for high-contrast headings and primary labels.
  - `--color-text-secondary`: Medium Gray (`#6b7280`) for body text and descriptions.
  - `--color-text-light`: Muted Gray (`#9ca3af`) for placeholders or disabled text.

## 3. Typography
- **Headings**: `--font-heading` (`Playfair Display`, serif). Used for `<h1>`, `<h2>`, and `.section-title` classes to give an elegant, professional aesthetic.
- **Body Text**: `--font-body` (`Inter`, sans-serif). Used for all other text to ensure maximum readability and a modern tech feel.

## 4. Component Styling Rules
- **CSS Architecture**: Use standard CSS files imported directly into components. Avoid Tailwind unless explicitly configured and requested.
- **Variables**: Always use `var(--variable-name)`.
- **Buttons**:
  - `.btn-primary`: Solid background (`var(--color-primary)`), white text, fully rounded (`border-radius: 30px`).
  - `.btn-secondary`: Transparent background, colored border, colored text.
  - All buttons must have a `transition: all var(--transition-fast)` for hover states.
- **Cards**:
  - Use `border-radius: var(--radius-md)` or `var(--radius-lg)`.
  - Apply `box-shadow: var(--shadow-md)` for subtle elevation.
- **Spacing**: Use consistent rem or pixel values (e.g., 8px, 16px, 24px, 32px) for gaps and padding to maintain a rhythmic grid.
