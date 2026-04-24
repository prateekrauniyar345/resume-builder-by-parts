"""
Utilities for loading resume parts, raw docs, and building final resumes.
"""

import os
from pathlib import Path
from datetime import datetime


class ResumeLoader:
    """Load resume parts and raw documentation."""

    RESUME_PARTS_DIR = Path(__file__).parent.parent / "resume-parts"
    RAW_DOCS_DIR = Path(__file__).parent.parent / "raw-docs"
    OUTPUT_DIR = Path(__file__).parent.parent / "output"

    @classmethod
    def load_resume_part(cls, part_name: str) -> str:
        """Load a single resume part."""
        file_path = cls.RESUME_PARTS_DIR / f"{part_name}.tex"
        if file_path.exists():
            return file_path.read_text(encoding="utf-8")
        return ""

    @classmethod
    def load_all_resume_parts(cls) -> dict:
        """Load all resume parts."""
        parts = {
            "head": cls.load_resume_part("head"),
            "skills": cls.load_resume_part("skills"),
            "education": cls.load_resume_part("education"),
            "experience": cls.load_resume_part("experience"),
            "projects": cls.load_resume_part("projects"),
            "tail": cls.load_resume_part("tail"),
        }
        return parts

    @classmethod
    def load_raw_docs(cls) -> str:
        """Load all raw documentation for candidate context."""
        docs_content = []
        
        if cls.RAW_DOCS_DIR.exists():
            for file_path in cls.RAW_DOCS_DIR.glob("*.md"):
                try:
                    docs_content.append(f"--- {file_path.name} ---\n")
                    docs_content.append(file_path.read_text(encoding="utf-8"))
                    docs_content.append("\n\n")
                except Exception as e:
                    print(f"Error loading {file_path}: {e}")
        
        return "".join(docs_content)

    @classmethod
    def create_context(cls) -> dict:
        """Create context dictionary with all resume parts and background info."""
        parts = cls.load_all_resume_parts()
        raw_docs = cls.load_raw_docs()
        
        context = {
            "skills": parts["skills"],
            "education": parts["education"],
            "experience": parts["experience"],
            "projects": parts["projects"],
            "background": raw_docs,
        }
        
        return context


class ResumeBuilder:
    """Build and save complete LaTeX resumes."""

    OUTPUT_DIR = Path(__file__).parent.parent / "output"

    @classmethod
    def build_resume(
        cls,
        job_title: str,
        optimized_sections: dict,
        head_section: str,
        tail_section: str,
    ) -> str:
        """
        Build a complete LaTeX resume from optimized sections.
        
        Args:
            job_title: The job title for naming the file
            optimized_sections: Dict with 'skills', 'education', 'experience', 'projects'
            head_section: The header section (name, contact info)
            tail_section: The tail section (certifications, awards)
            
        Returns:
            The complete LaTeX resume as string
        """
        
        # Combine sections in order
        # Note: head_section already contains \begin{document}
        # tail_section should contain \end{document}
        resume_parts = [
            head_section.rstrip(),
            optimized_sections.get("skills", "").strip(),
            optimized_sections.get("education", "").strip(),
            optimized_sections.get("experience", "").strip(),
            optimized_sections.get("projects", "").strip(),
            tail_section.strip(),
        ]
        
        # Filter out empty parts and join with proper newlines
        non_empty_parts = [part for part in resume_parts if part]
        complete_resume = "\n".join(non_empty_parts)
        
        return complete_resume

    @classmethod
    def save_resume(cls, resume_content: str, job_title: str) -> str:
        """
        Save the resume to a file.
        
        Args:
            resume_content: The complete LaTeX resume
            job_title: Job title for the filename
            
        Returns:
            Path to the saved file
        """
        
        cls.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        
        # Create filename with timestamp and job title
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_job_title = "".join(
            c if c.isalnum() or c in " -_" else "" for c in job_title
        ).replace(" ", "_")
        filename = f"Resume_{safe_job_title}_{timestamp}.tex"
        
        file_path = cls.OUTPUT_DIR / filename
        file_path.write_text(resume_content, encoding="utf-8")
        
        return str(file_path)

    @classmethod
    def generate_and_save(
        cls,
        job_title: str,
        optimized_sections: dict,
    ) -> dict:
        """
        Generate and save the complete resume.
        
        Args:
            job_title: Job title for naming
            optimized_sections: Optimized resume sections
            
        Returns:
            Dictionary with resume content and file path
        """
        
        # Load head and tail from original files
        loader = ResumeLoader()
        head = loader.load_resume_part("head")
        tail = loader.load_resume_part("tail")
        
        # Build complete resume
        complete_resume = cls.build_resume(job_title, optimized_sections, head, tail)
        
        # Save to file
        file_path = cls.save_resume(complete_resume, job_title)
        
        return {
            "content": complete_resume,
            "file_path": file_path,
            "filename": Path(file_path).name,
        }
