from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
import html
import re


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
DOCS.mkdir(exist_ok=True)


SLIDES = [
    ("AI-Powered Study Assistant Telegram Bot", ["Python final project", "Telegram Bot + Groq API"]),
    ("Проблема", ["Студентам часто нужна быстрая помощь во время учебы.", "Нужно объяснять темы, создавать quiz и сохранять заметки."]),
    ("Решение", ["Telegram-бот работает как AI study assistant.", "Пользователь задает вопрос, а бот отвечает через Groq API."]),
    ("Технологии", ["Python", "Telegram Bot API", "Groq API", "JSON and CSV", "unittest", "Git and GitHub"]),
    ("Команды бота", ["/start - welcome", "/help - commands", "/ask - AI answer", "/quiz - quiz", "/note and /notes - notes", "/stats - statistics"]),
    ("Архитектура", ["main.py - запуск", "bot.py - Telegram logic", "groq_client.py - AI API", "data_manager.py - files", "models.py - OOP", "tests/ - unit tests"]),
    ("Groq API", ["Бот получает вопрос от пользователя.", "GroqClient отправляет prompt в Groq API.", "Ответ возвращается пользователю в Telegram."]),
    ("Работа с данными", ["notes.json хранит заметки.", "history.csv хранит историю действий.", "os module создает папку data."]),
    ("OOP", ["Classes: StudyAssistantBot, DataManager, GroqClient.", "Inheritance: QuizSession inherits StudySession.", "Polymorphism: describe() works differently."]),
    ("Python topics", ["Variables and data types", "Conditions and loops", "Collections", "Functions", "Decorators", "Iterators and generators", "Regular expressions"]),
    ("Testing", ["Unit tests are stored in tests/.", "Command: python -m unittest discover tests", "Tests check text tools and data manager."]),
    ("Conclusion", ["The project is a real-world Python application.", "It is useful, readable, and covers the main course topics."]),
]


def xml(text: str) -> str:
    return html.escape(text, quote=True)


def make_docx() -> None:
    markdown = (ROOT / "REPORT_RU.md").read_text(encoding="utf-8")
    paragraphs = []

    for line in markdown.splitlines():
        line = line.strip()
        if not line or line.startswith("```"):
            continue

        if line.startswith("# "):
            style = "Title"
            text = line[2:]
        elif line.startswith("## "):
            style = "Heading1"
            text = line[3:]
        elif line.startswith("### "):
            style = "Heading2"
            text = line[4:]
        elif line.startswith("- "):
            style = "ListParagraph"
            text = "• " + line[2:]
        else:
            style = "Normal"
            text = re.sub(r"`([^`]+)`", r"\1", line)
            text = text.replace("**", "")

        paragraphs.append(
            f'<w:p><w:pPr><w:pStyle w:val="{style}"/></w:pPr>'
            f"<w:r><w:t>{xml(text)}</w:t></w:r></w:p>"
        )

    document_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        f"<w:body>{''.join(paragraphs)}"
        "<w:sectPr><w:pgSz w:w=\"11906\" w:h=\"16838\"/>"
        "<w:pgMar w:top=\"1440\" w:right=\"1440\" w:bottom=\"1440\" w:left=\"1440\"/>"
        "</w:sectPr></w:body></w:document>"
    )

    styles_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        '<w:style w:type="paragraph" w:styleId="Normal"><w:name w:val="Normal"/></w:style>'
        '<w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:rPr><w:b/><w:sz w:val="36"/></w:rPr></w:style>'
        '<w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:rPr><w:b/><w:sz w:val="28"/></w:rPr></w:style>'
        '<w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/><w:rPr><w:b/><w:sz w:val="24"/></w:rPr></w:style>'
        '<w:style w:type="paragraph" w:styleId="ListParagraph"><w:name w:val="List Paragraph"/></w:style>'
        "</w:styles>"
    )

    content_types = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Default Extension="xml" ContentType="application/xml"/>'
        '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
        '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>'
        "</Types>"
    )

    root_rels = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>'
        "</Relationships>"
    )

    doc_rels = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
        "</Relationships>"
    )

    with ZipFile(DOCS / "Report_RU.docx", "w", ZIP_DEFLATED) as docx:
        docx.writestr("[Content_Types].xml", content_types)
        docx.writestr("_rels/.rels", root_rels)
        docx.writestr("word/document.xml", document_xml)
        docx.writestr("word/styles.xml", styles_xml)
        docx.writestr("word/_rels/document.xml.rels", doc_rels)


def slide_xml(title: str, bullets: list[str], slide_number: int) -> str:
    bullet_shapes = []
    y = 1700000
    for bullet in bullets:
        bullet_shapes.append(
            f'<p:sp><p:nvSpPr><p:cNvPr id="{slide_number * 10 + len(bullet_shapes) + 2}" name="Bullet"/>'
            '<p:cNvSpPr/><p:nvPr/></p:nvSpPr><p:spPr><a:xfrm>'
            f'<a:off x="900000" y="{y}"/><a:ext cx="7800000" cy="420000"/></a:xfrm></p:spPr>'
            '<p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:r><a:rPr lang="en-US" sz="2400"/>'
            f"<a:t>{xml('• ' + bullet)}</a:t></a:r></a:p></p:txBody></p:sp>"
        )
        y += 520000

    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" '
        'xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">'
        '<p:cSld><p:bg><p:bgPr><a:solidFill><a:srgbClr val="F7F9FC"/></a:solidFill></p:bgPr></p:bg>'
        '<p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>'
        '<p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>'
        f'<p:sp><p:nvSpPr><p:cNvPr id="{slide_number * 10 + 1}" name="Title"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>'
        '<p:spPr><a:xfrm><a:off x="700000" y="520000"/><a:ext cx="8200000" cy="750000"/></a:xfrm></p:spPr>'
        '<p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:r><a:rPr lang="en-US" sz="3600" b="1"><a:solidFill><a:srgbClr val="16324F"/></a:solidFill></a:rPr>'
        f"<a:t>{xml(title)}</a:t></a:r></a:p></p:txBody></p:sp>"
        f"{''.join(bullet_shapes)}</p:spTree></p:cSld><p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr></p:sld>"
    )


def make_pptx() -> None:
    slide_overrides = "".join(
        f'<Override PartName="/ppt/slides/slide{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>'
        for i in range(1, len(SLIDES) + 1)
    )
    content_types = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Default Extension="xml" ContentType="application/xml"/>'
        '<Override PartName="/ppt/presentation.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/>'
        f"{slide_overrides}</Types>"
    )
    root_rels = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="ppt/presentation.xml"/>'
        "</Relationships>"
    )
    slide_ids = "".join(
        f'<p:sldId id="{255 + i}" r:id="rId{i}"/>' for i in range(1, len(SLIDES) + 1)
    )
    presentation_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<p:presentation xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" '
        'xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">'
        f"<p:sldIdLst>{slide_ids}</p:sldIdLst><p:sldSz cx=\"9144000\" cy=\"5143500\" type=\"screen16x9\"/>"
        "<p:notesSz cx=\"6858000\" cy=\"9144000\"/></p:presentation>"
    )
    presentation_rels = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        + "".join(
            f'<Relationship Id="rId{i}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide{i}.xml"/>'
            for i in range(1, len(SLIDES) + 1)
        )
        + "</Relationships>"
    )

    with ZipFile(DOCS / "AI_Study_Assistant_Presentation.pptx", "w", ZIP_DEFLATED) as pptx:
        pptx.writestr("[Content_Types].xml", content_types)
        pptx.writestr("_rels/.rels", root_rels)
        pptx.writestr("ppt/presentation.xml", presentation_xml)
        pptx.writestr("ppt/_rels/presentation.xml.rels", presentation_rels)
        for index, (title, bullets) in enumerate(SLIDES, start=1):
            pptx.writestr(f"ppt/slides/slide{index}.xml", slide_xml(title, bullets, index))


if __name__ == "__main__":
    make_docx()
    make_pptx()
    print("Generated docs/Report_RU.docx")
    print("Generated docs/AI_Study_Assistant_Presentation.pptx")
