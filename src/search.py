"""Search every Word document in the corpus for a user-provided keyword."""

from pathlib import Path

from docx import Document


# Store the folder path relative to the repository root.
CORPUS_DIR = Path(__file__).parent.parent / "corpus"


def read_paragraphs(docx_path):
	"""Return the non-empty paragraphs from one Word document."""
	# Open the .docx file and collect paragraph text in document order.
	document = Document(docx_path)
	return [paragraph.text for paragraph in document.paragraphs if paragraph.text.strip()]


def search_corpus(keyword):
	"""Print every paragraph containing keyword and its source filename."""
	# Compare lowercase text so searches are not affected by capitalization.
	normalized_keyword = keyword.casefold()

	# Find all .docx files and keep the output order predictable.
	docx_files = sorted(
		path for path in CORPUS_DIR.glob("*.docx") if not path.name.startswith("~$")
	)

	# Read each document and print paragraphs that contain the keyword.
	for docx_path in docx_files:
		for paragraph in read_paragraphs(docx_path):
			if normalized_keyword in paragraph.casefold():
				print(f"{docx_path.name}: {paragraph}")


def main():
	"""Validate inputs, ask for a keyword, and search the corpus."""
	# Stop with a clear message if the expected corpus folder is missing.
	if not CORPUS_DIR.is_dir():
		raise SystemExit(f"No corpus folder found at {CORPUS_DIR}")

	# Ask the user what text to find in the Word documents.
	keyword = input("Enter a keyword: ").strip()
	if not keyword:
		raise SystemExit("Please enter a keyword.")

	search_corpus(keyword)


# Run the search only when this file is executed as a script.
if __name__ == "__main__":
	main()
