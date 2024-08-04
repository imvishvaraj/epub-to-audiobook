import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup


file_name = ''

# Read the EPUB file
book = epub.read_epub(file_name)

# Get all document items (chapters) from the book
chapters = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))


def chapter_to_str(chapter):
    soup = BeautifulSoup(chapter.get_body_content(), 'html.parser')
    text = [para.get_text() for para in soup.find_all('p')]
    return ' '.join(text)


# Collect the text of each chapter
texts = {}
for c in chapters:
    texts[c.get_name()] = chapter_to_str(c)

# Print the collected texts
for chapter_name, chapter_text in texts.items():
    print(f"Chapter: {chapter_name}\n{chapter_text}\n")
    break
