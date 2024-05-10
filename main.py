from summarize_utils import get_pdf_text, get_sections, load_pdf, make_xml_file, write_markdown
from save_db_utils import add_notion_db_page,write_notion_db_page
from paper_letter import get_summary
import arxiv
import sys


def main(args):
    arxiv_id = args[1]
  
    # PDFファイルを取得
    print(arxiv_id)
    paper = next(arxiv.Search(id_list=[arxiv_id]).results())
    # thread_text = f"paper: 1本目\n" + get_summary(paper)
    with open("./tmp.txt", mode="r") as f:
        thread_text = f.read()
    print(thread_text)
    # pdf_file_name, pdf_file_path = load_pdf(thread_text)

    # # セクション分割して，要約した文章を作成
    # root = make_xml_file(pdf_file_name)
    # sections = get_sections(root)
    # pdf_text = get_pdf_text(pdf_file_path)
    # # markdown_text = write_markdown(sections, pdf_text.split(" "), pdf_file_name)
    # # for debug
    # # ここでtext類を保存する
    
    # with open("./tmp_section.txt", mode="w") as f:
    #     for d in sections:
    #         f.write(f"{d.title},  {d.body}\n")
    # with open("./tmp_pdf_text.txt", mode="w") as f:
    #     f.write(pdf_text)
        
    # with open("./tmp.txt", mode="w") as f:
    #     f.write(thread_text)
    # with open("./tmp_markdown.txt", mode="w") as f:
    #     f.write(markdown_text)


    with open("./tmp.txt", mode="r") as f:
        thread_text = f.read()
    with open("./tmp_markdown.txt", mode="r") as f:
        markdown_text = f.read()

    # Notionにページを作成し，要約を書き込む
    paper, database_id = add_notion_db_page(thread_text, is_debug=True)
    
    # write_notion_db_page(markdown_text, paper, database_id, is_debug=True)
    
if __name__ == "__main__" :
    args = sys.argv
    main(args)