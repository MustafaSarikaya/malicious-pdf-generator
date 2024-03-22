from pdfalyzer.decorators.pdf_tree_node import PdfTreeNode
from pdfalyzer.pdfalyzer import Pdfalyzer
from anytree.search import findall_by_attr


def check_open_action(pdf_path: str) -> bool:
    pdfalyzer = Pdfalyzer(pdf_path)
    try:
        page_nodes = findall_by_attr(pdfalyzer.pdf_tree, name='type', value='/Catalog')

        catalog_node = page_nodes[0]

        catalog_node_children = catalog_node.children[1]

        print(f"the file {pdf_path} has {catalog_node_children} OpenAction")

        return str(catalog_node_children) == "<4:Action:JavaScript(Dictionary)>"

    except Exception as e:
        print(f"Error: {e}")
        return False
