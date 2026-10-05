# Business Requirements Document (BRD)
**Project Name:** AI & Data Science Education vs. Labor Market Dashboard
**Target Agent:** Antigravity (Dashboard Development Agent)

## 1. Project Overview
**วัตถุประสงค์:** พัฒนา Interactive Dashboard เพื่อวิเคราะห์และเปรียบเทียบข้อมูลการผลิตบัณฑิต (Supply) และความต้องการของตลาดแรงงาน (Demand) ในสายงาน AI, Data Science และ Statistics รวมถึงการวิเคราะห์ช่องว่างทางทักษะ (Skills Mismatch)

**Technical Stack Requirements:**
*   **Backend & Framework:** Python (ใช้ Dash by Plotly สำหรับการสร้าง Web Application)
*   **Data Visualization:** Plotly (ใช้สร้าง Interactive Graphs)
*   **Interactivity:** กราฟทุกตัวในแต่ละ Tab ต้องมีการเชื่อมโยงกัน (Cross-filtering) เมื่อผู้ใช้คลิกเลือกข้อมูลในกราฟหนึ่ง กราฟอื่นๆ ใน Tab เดียวกันจะต้องอัปเดตตามข้อมูลที่เลือก (ใช้ Dash Callbacks)

---

## 2. Dashboard Structure & Functional Requirements
Dashboard แบ่งออกเป็น 3 Tabs หลัก ดังนี้:

### Tab 1: ปริมาณคนที่จบและ Skills ที่เรียนมา (Education & Supply)
**เป้าหมาย:** แสดงข้อมูลหลักสูตรที่ผลิตบัณฑิต ทักษะที่สอน อัตราการได้งาน และต้นทุนการศึกษา
**UI Components & Charts:**
1.  **ปริมาณการผลิตบัณฑิต (Graduates Volume):**
    *   **ประเภทกราฟ:** Stacked Bar Chart หรือ Multi-line Chart
    *   **แกน X:** ปีการศึกษา (Year)
    *   **แกน Y:** จำนวนบัณฑิต (Number of Graduates)
    *   **แบ่งกลุ่ม (Color/Legend):** ชื่อหลักสูตร (Program Name) เช่น B.Sc. Data Science, M.Sc. AI, B.Sc. Statistics
2.  **รายวิชาบังคับ/ทักษะที่เรียน (Core Courses & Learned Skills):**
    *   **ประเภทกราฟ:** Horizontal Bar Chart หรือ Treemap
    *   **ข้อมูลที่แสดง:** รายชื่อวิชาบังคับ (Core Courses) ที่สอดคล้องกับสายงาน และทักษะที่ได้จากวิชานั้นๆ
    *   **Interactivity:** หากคลิกเลือกหลักสูตรจากกราฟที่ 1 กราฟนี้จะฟิลเตอร์แสดงเฉพาะวิชาของหลักสูตรนั้น
3.  **อัตราการได้งานหลังเรียนจบ (Employment Rate Post-Graduation):**
    *   **ประเภทกราฟ:** Grouped Bar Chart
    *   **แกน X:** ปีที่เรียนจบ (Cohort)
    *   **แกน Y:** เปอร์เซ็นต์/จำนวนบัณฑิตที่ได้งาน
    *   **แบ่งกลุ่ม (Group):** ได้งานทำในปีแรก (Year 1), ปีที่สอง (Year 2), ปีที่สาม (Year 3)
4.  **ค่าเทอม (Tuition Fees):**
    *   **ประเภทกราฟ:** KPI Card พร้อม Scatter Plot หรือ Bar Chart
    *   **ข้อมูลที่แสดง:** เปรียบเทียบค่าเทอมตลอดหลักสูตรของแต่ละสาขา

---

### Tab 2: ปริมาณงานที่จ้างและ Skills งานที่ต้องการ (Labor Market & Demand)
**เป้าหมาย:** แสดงภาพรวมของตลาดแรงงาน ความต้องการทักษะ และผลตอบแทน
**UI Components & Charts:**
1.  **ปริมาณตำแหน่งงานที่ว่าง (Job Vacancies Volume):**
    *   **ประเภทกราฟ:** Area Chart หรือ Bar Chart
    *   **แกน X:** ช่วงเวลา (เดือน/ปี)
    *   **แกน Y:** จำนวนตำแหน่งงานที่เปิดรับ (Number of Job Openings)
    *   **แบ่งกลุ่ม (Color):** Job Title (เช่น AI Engineer, Data Analyst, Data Scientist)
2.  **ทักษะที่ตลาดต้องการ (Required Skills):**
    *   **ประเภทกราฟ:** Horizontal Bar Chart หรือ Word Cloud
    *   **ข้อมูลที่แสดง:** ทักษะที่ถูกระบุใน Job Description มากที่สุด เรียงตามความถี่ (Frequency)
3.  **บริษัทที่เปิดรับบุคลากร (Hiring Companies):**
    *   **ประเภทกราฟ:** Bubble Chart หรือ ตารางข้อมูล (DataTable)
    *   **ข้อมูลที่แสดง:** ชื่อบริษัท, อุตสาหกรรม (Industry), และจำนวนตำแหน่งที่เปิดรับ
    *   **Interactivity:** เมื่อคลิกที่ทักษะในกราฟที่ 2 กราฟนี้จะโชว์ว่ามีบริษัทไหนบ้างที่ต้องการทักษะนั้น
4.  **เงินเดือนตามระดับประสบการณ์ (Salary by Experience Level):**
    *   **ประเภทกราฟ:** Box Plot หรือ Violin Plot
    *   **แกน X:** ระดับการทำงาน (Entry-level, Mid-level, Senior, Executive)
    *   **แกน Y:** ฐานเงินเดือน (Salary Range)

---

### Tab 3: การวิเคราะห์ช่องว่างทางทักษะ (Skills Mismatch Analysis)
**เป้าหมาย:** นำข้อมูลทักษะที่สอน (Tab 1) มาเปรียบเทียบกับทักษะที่ตลาดต้องการ (Tab 2) เพื่อดูว่ามีทักษะใดที่ขาดแคลนหรือล้นตลาด
**UI Components & Charts:**
1.  **Skills Supply vs Demand Comparison:**
    *   **ประเภทกราฟ:** Diverging Bar Chart หรือ Radar Chart
    *   **ข้อมูลที่แสดง:** แกนหนึ่งแสดงเปอร์เซ็นต์ของหลักสูตรที่มีการสอนทักษะนั้น (Supply) อีกแกนแสดงเปอร์เซ็นต์ของตำแหน่งงานที่ต้องการทักษะนั้น (Demand)
2.  **Mismatch Gap Identifier:**
    *   **ประเภทกราฟ:** Scatter Plot (Quadrant Analysis)
    *   **แกน X:** ความต้องการของตลาด (Demand/Required Skills)
    *   **แกน Y:** การผลิตจากมหาวิทยาลัย (Supply/Learned Skills)
    *   **การวิเคราะห์:** 
        *   High Demand & Low Supply = ขาดแคลน (Critical Shortage)
        *   Low Demand & High Supply = ล้นตลาด (Oversupply)

---

## 3. Implementation Instructions for Antigravity
1.  **Mock Data Generation:** เนื่องจากยังไม่มี Database จริง ขอให้สร้าง Mock Data (Pandas DataFrame) สำหรับโครงสร้างข้อมูลทั้ง 3 Tabs เพื่อใช้ในการ Render กราฟ
2.  **Dashboard Layout:** สร้างโครงสร้างแอปพลิเคชันโดยใช้ `dash-bootstrap-components` เพื่อให้ดูเป็นมืออาชีพ มีแถบนำทาง (Tabs) ที่ชัดเจน
3.  **Cross-Filtering Logic:** ให้เขียนฟังก์ชัน `@app.callback` เพื่อดักจับเหตุการณ์ `clickData` จากกราฟหลัก และนำค่าเหล่านั้นไปเป็น Filter condition ให้กับ Pandas DataFrame ของกราฟอื่นๆ ใน Tab เดียวกัน