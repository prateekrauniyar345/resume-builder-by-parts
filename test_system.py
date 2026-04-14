"""
Test helper script to validate the resume optimization system.
Run this to test all components before launching the full application.
"""

import json
import requests
from pathlib import Path
import sys

BACKEND_URL = "http://localhost:8000"
TEST_JOB_DESCRIPTION = """
We're looking for a talented Full Stack Engineer to join our team.

Requirements:
- 3+ years of experience with React.js or Next.js
- Strong backend experience with Python (FastAPI, Django) or Node.js
- Experience with PostgreSQL, MongoDB, or similar databases
- Git version control and CI/CD pipelines
- RESTful API design and implementation
- Experience with Docker and containerization
- Strong understanding of authentication (OAuth, JWT)
- Testing expertise (unit, integration, e2e tests)

Nice to have:
- Experience with machine learning models
- Cloud platforms (AWS, Azure, GCP)
- GraphQL experience
- Experience with microservices architecture
- Technical leadership or mentoring experience

Responsibilities:
- Build scalable web applications
- Design and implement robust APIs
- Optimize application performance
- Collaborate with product and design teams
- Write clean, tested, maintainable code
- Participate in code reviews
"""


def test_health():
    """Test API health check."""
    print("Testing API health check...")
    try:
        response = requests.get(f"{BACKEND_URL}/health", timeout=5)
        if response.status_code == 200:
            print("✓ Backend is running and healthy")
            return True
        else:
            print(f"✗ Backend returned status {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("✗ Cannot connect to backend. Make sure it's running on http://localhost:8000")
        return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False


def test_resume_parts():
    """Test resume parts loading."""
    print("Testing resume parts loading...")
    try:
        response = requests.get(f"{BACKEND_URL}/resume-parts", timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "success":
                parts = data.get("parts", {})
                print(f"✓ Loaded {len(parts)} resume parts")
                for part_name, content in parts.items():
                    print(f"  - {part_name}: {len(content)} chars")
                return True
            else:
                print("✗ Unexpected response format")
                return False
        else:
            print(f"✗ Server returned status {response.status_code}")
            return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False


def test_optimization(job_title="Full Stack Engineer"):
    """Test the full optimization workflow."""
    print(f"Testing resume optimization for '{job_title}'...")
    try:
        payload = {
            "job_description": TEST_JOB_DESCRIPTION,
            "job_title": job_title,
        }

        print("Sending optimization request (this may take 30-60 seconds)...")
        response = requests.post(
            f"{BACKEND_URL}/optimize-resume",
            json=payload,
            timeout=120,  # 2 minute timeout for agent processing
        )

        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "success":
                print("✓ Resume optimization successful!")
                print(f"  - Message: {data.get('message')}")
                print(f"  - File saved to: {data.get('file_path')}")
                print(f"  - Filename: {data.get('filename')}")

                # Check if file was actually created
                file_path = Path(data.get("file_path", ""))
                if file_path.exists():
                    file_size = file_path.stat().st_size
                    print(f"  - File size: {file_size} bytes")
                    print("✓ File successfully created")
                    return True
                else:
                    print("✗ File not created at the expected path")
                    return False
            else:
                print(f"✗ Optimization failed: {data.get('message')}")
                return False
        elif response.status_code == 400:
            error_data = response.json()
            print(f"✗ Bad request: {error_data.get('detail')}")
            print("  Make sure job description is at least 50 characters")
            return False
        else:
            print(f"✗ Server returned status {response.status_code}")
            print(f"  Response: {response.text}")
            return False

    except requests.exceptions.Timeout:
        print("✗ Request timed out. Agent processing took too long.")
        print("  This could mean:")
        print("  - Your LLM API key is not configured")
        print("  - The API is experiencing issues")
        print("  - Network connection problem")
        return False
    except requests.exceptions.ConnectionError:
        print("✗ Cannot connect to backend")
        return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False


def test_output_directory():
    """Test output directory retrieval."""
    print("Testing output directory...")
    try:
        response = requests.get(f"{BACKEND_URL}/output-directory", timeout=5)
        if response.status_code == 200:
            data = response.json()
            output_dir = Path(data.get("output_directory", ""))
            print(f"✓ Output directory: {output_dir}")
            if output_dir.exists():
                print(f"  - Directory exists")
                files = list(output_dir.glob("*.tex"))
                print(f"  - Generated resumes: {len(files)}")
                if files:
                    for file in sorted(files)[-3:]:  # Show last 3
                        print(f"    - {file.name}")
            else:
                print(f"  - Note: Directory will be created on first optimization")
            return True
        else:
            print(f"✗ Server returned status {response.status_code}")
            return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False


def main():
    """Run all tests."""
    print("\n" + "=" * 60)
    print("Resume Optimizer - System Test")
    print("=" * 60 + "\n")

    results = {
        "health": test_health(),
        "resume_parts": test_resume_parts(),
        "output_directory": test_output_directory(),
    }

    print("\n" + "-" * 60)
    print("Optional: Test Full Optimization (requires LLM API key)")
    print("-" * 60 + "\n")

    try:
        results["optimization"] = test_optimization()
    except Exception as e:
        print(f"Skipping optimization test: {e}")
        results["optimization"] = None

    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)

    for test_name, passed in results.items():
        if passed is None:
            status = "⊘ Skipped"
        elif passed:
            status = "✓ Passed"
        else:
            status = "✗ Failed"
        print(f"{test_name:20} {status}")

    print("=" * 60 + "\n")

    # Return exit code based on results
    all_passed = all(v is True for v in results.values() if v is not None)
    if all_passed:
        print("✓ All tests passed! Your system is ready.")
        return 0
    else:
        print("✗ Some tests failed. Check the output above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
