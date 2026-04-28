"""
GY462 Material Downloader
Run this script after logging in to Moodle in the browser.
It will download all PDFs to the local folders.
"""

import asyncio
import os
from pathlib import Path
from playwright.async_api import async_playwright

BASE_DIR = Path(__file__).parent

FILES = {
    "past-exams": [
        ("GY462_2025_Exam_Solutions.pdf", "https://moodle.lse.ac.uk/pluginfile.php/5787017/mod_resource/content/1/GY462%202025%20Exam%20with%20Solutions.pdf"),
        ("GY462_2024.pdf", "https://moodle.lse.ac.uk/pluginfile.php/4378222/mod_resource/content/1/GY462%202024.pdf"),
        ("GY462_2023_Solutions.pdf", "https://moodle.lse.ac.uk/pluginfile.php/4378223/mod_resource/content/1/GY462%20Exam%202023%20Solutions.pdf"),
        ("GY462_2022.pdf", "https://moodle.lse.ac.uk/pluginfile.php/4378224/mod_resource/content/1/GY462%20Exam%202021-22.pdf"),
        ("GY462_2021_Solutions.pdf", "https://moodle.lse.ac.uk/pluginfile.php/4378225/mod_resource/content/1/GY462%20Quetions%20and%20Solutions%202021%20Draft.pdf"),
        ("GY462_2020_Solutions.pdf", "https://moodle.lse.ac.uk/pluginfile.php/4378226/mod_resource/content/1/GY462%20Questions%20and%20Solutions%202020%20Final.pdf"),
        ("GY462_2019_Solutions.pdf", "https://moodle.lse.ac.uk/pluginfile.php/4378227/mod_resource/content/5/amended%202019%20solutions.pdf"),
        ("GY462_2018.pdf", "https://moodle.lse.ac.uk/pluginfile.php/4378228/mod_resource/content/1/GY462Questions2018_Checked.pdf"),
    ],
    "lectures": [
        ("Lecture3_Full.pdf", "https://moodle.lse.ac.uk/pluginfile.php/5762813/mod_resource/content/2/GY462_Lec03_2026_lec_full_page.pdf"),
        ("Lecture4_Full.pdf", "https://moodle.lse.ac.uk/pluginfile.php/5766352/mod_resource/content/1/GY462_Lec04_2026_lec_full_page.pdf"),
        ("Syllabus_WT2026.pdf", "https://moodle.lse.ac.uk/pluginfile.php/4378205/mod_resource/content/3/GY462%20Syllabus%20WT2026%20Final.pdf"),
    ],
    "problem-sets": [
        ("ProblemSet1_2026.pdf", "https://moodle.lse.ac.uk/pluginfile.php/5759562/mod_resource/content/0/Problem%20Set%201_2026.pdf"),
        ("ProblemSet1_Solutions.pdf", "https://moodle.lse.ac.uk/pluginfile.php/5767386/mod_resource/content/0/Problem%20Set%201%20Solutions_2026.pdf"),
        ("ProblemSet1_FinancialCalc.pdf", "https://moodle.lse.ac.uk/pluginfile.php/5767387/mod_resource/content/0/Problem%20Set%201%20-%20Financial%20calculator.pdf"),
        ("ProblemSet2_2026.pdf", "https://moodle.lse.ac.uk/pluginfile.php/5770242/mod_resource/content/0/Problem%20Set%202_2026.pdf"),
        ("ProblemSet2_Solutions.pdf", "https://moodle.lse.ac.uk/pluginfile.php/5771643/mod_resource/content/0/Problem%20Set%202%20Solutions%202026.pdf"),
    ],
    "seminars": [
        ("Seminar1_Slides.pdf", "https://moodle.lse.ac.uk/pluginfile.php/5767388/mod_resource/content/0/Seminar%201%20Slides_2026.pdf"),
        ("Seminar1_Perpetuity_Demo.pdf", "https://moodle.lse.ac.uk/pluginfile.php/4378251/mod_resource/content/0/Seminar%201%20Slides%20-%20Perpetuity%20demonstration.pdf"),
    ],
}

async def download_all():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(accept_downloads=True)
        page = await context.new_page()

        await page.goto("https://moodle.lse.ac.uk/course/view.php?id=12300")
        print("\n>>> 请在浏览器中登录 LSE Moodle，然后回到终端按 Enter 继续...")
        input()

        total = sum(len(v) for v in FILES.values())
        done = 0

        for folder, file_list in FILES.items():
            target_dir = BASE_DIR / folder
            target_dir.mkdir(exist_ok=True)

            for filename, url in file_list:
                target_path = target_dir / filename
                if target_path.exists():
                    print(f"  ✓ 已存在: {filename}")
                    done += 1
                    continue

                try:
                    async with context.expect_download(timeout=30_000) as dl_info:
                        await page.goto(url)
                    download = await dl_info.value
                    await download.save_as(target_path)
                    done += 1
                    print(f"  [{done}/{total}] 下载完成: {filename}")
                except Exception as e:
                    print(f"  [!] 下载失败: {filename} — {e}")

        await browser.close()
        print(f"\n✅ 全部完成！文件保存在: {BASE_DIR}")

if __name__ == "__main__":
    asyncio.run(download_all())
