# 🎨 UI-Refined Business Requirements Document (BRD)

**Project Name:** AI & Data Science Education vs. Labor Market Dashboard
**Target Agent:** Antigravity (Dashboard Development Agent)
**Design Reference File:** `image_d15cca.png`

## 1. UI/UX & Styling Guidelines (Strict Requirements)

The dashboard must strictly adhere to the visual design language presented in `image_d15cca.png`. 

*   **Overall Theme:** Light, modern, and clean with a masonry/grid card layout.
*   **Background Color:** Very light cyan/blue-grey tint for the main dashboard area.
*   **Card Styling:** White background (`#FFFFFF`), prominent rounded corners (approx. `border-radius: 15px`), and soft, subtle drop shadows to create depth. No harsh borders.
*   **Color Palette (Mandatory):**
    *   **Primary/Sidebar:** Vibrant Teal/Cyan (approx. `#00C4CC` to `#00D2D3`)
    *   **Accent 1 (Warm):** Golden Yellow / Orange (approx. `#FFCA28` to `#FFA726`)
    *   **Accent 2 (Cool):** Soft Purple / Indigo (approx. `#7E57C2` to `#5C6BC0`)
    *   **Text:** Dark Grey for primary headings, light muted grey for subtitles/axis labels.
*   **Typography:** Sans-serif, clean, rounded fonts (e.g., Poppins, Nunito, or Montserrat).

## 2. Structural Layout & Navigation

Based on `image_d15cca.png`, the layout must be divided into two main sections:

### A. Left Sidebar (Navigation)
*   **Style:** Fixed width, full height, solid Teal/Cyan background.
*   **Elements:** 
    *   Top: Circular user avatar icon (white outline/yellow fill).
    *   Middle: Stack of white, minimalist icons representing the Tabs (Home/Tab 1, Chat/Tab 2, Star/Tab 3, Settings, Menu list). The active tab icon should have a distinct state (e.g., background highlight).
    *   Bottom: Exit/Logout icon.
*   **Function:** Clicking the icons will switch between the 3 data Tabs defined in the original BRD (Supply, Demand, Mismatch).

### B. Main Content Area (Top Bar & Grid)
*   **Top Right:** A rounded search bar with a Teal search icon button.
*   **Grid System:** The dashboard uses an irregular grid system with widgets of varying widths and heights.

## 3. Widget Mapping (Tab 1 Example Layout)

To match the visual layout of `image_d15cca.png` precisely, map the **Tab 1 (Education & Supply)** data to the visual components as follows:

### Top Row Widgets
1.  **Top Left (Small Line Chart):** Single purple smooth line chart with a yellow tooltip. 
    *   *Data:* Total AI/DS Graduates over time.
2.  **Top Middle-Left (Small Line Chart):** Yellow line with data points.
    *   *Data:* Year-over-year growth rate of graduates.
3.  **Top Middle-Right (Calendar):** A clean calendar widget highlighting the current date.
4.  **Top Right (Two Donut Charts):** Two circular progress rings (one orange, one purple).
    *   *Data:* Total Male vs. Female graduates (or Masters vs. PhDs). Display numbers like "25K" and "90K" in the center.

### Middle Row Widgets
5.  **Middle Left (Dual KPIs):** Two simple numbers with mini sparklines beneath them.
    *   *Data:* "1205" (Data Science courses available) and "840" (AI courses available).
6.  **Center (Large Radial Progress):** A large teal circle showing a percentage, with a yellow CTA button below it.
    *   *Data:* "75%" - Overall Employment Rate Post-Graduation.
7.  **Right (Large Dual Line/Area Chart):** Smooth intersecting lines (purple and yellow) with a time axis.
    *   *Data:* Number of graduates who secured jobs in Year 1 (Yellow) vs. Year 2 (Purple) after graduation.

### Bottom Row Widgets
8.  **Bottom Left (Vertical Diverging Bar Chart):** Teal, yellow, and purple bars crossing a horizontal zero-line.
    *   *Data:* Skills supply surplus vs. deficit (Mismatch preview).
9.  **Bottom Center (Timeline/Process Bar):** A horizontal line with teal/green indicator nodes above and yellow nodes below.
    *   *Data:* Average timeline from graduation to employment by degree type.
10. **Bottom Right (Grouped Bar Chart):** Blue, cyan, and yellow vertical bars grouped by days (or in our case, years/cohorts).
    *   *Data:* Tuition Fees comparison (B.Sc., M.Sc., PhD) across different academic years.
11. **Bottom Extreme Left (Small Stacked Horizontal Bar):** A thin progress bar showing distribution.
    *   *Data:* Proportion of graduates by faculty/department.

## 4. Instructions for Antigravity
1.  **CSS/Styling:** Prioritize exact CSS replication of `image_d15cca.png`. The dashboard must look exactly like the design reference before applying the complex Dash/Plotly callbacks.
2.  **Plotly Theming:** Configure `plotly.graph_objects` or `plotly.express` templates to strip away default grid lines, use transparent backgrounds for the charts, and apply the exact hex codes mentioned above to line and bar colors.
3.  **Framework:** Continue using Python with Dash by Plotly. Use CSS Grid or Flexbox within `dash-html-components` to achieve the specific masonry card arrangement shown in the image.