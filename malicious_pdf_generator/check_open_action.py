from pdfalyzer.pdfalyzer import Pdfalyzer
from anytree.search import findall_by_attr


def check_open_action(pdf_path: str) -> bool:
    """
    Checks if a given PDF file has an OpenAction that is a JavaScript action.

    Parameters:
        pdf_path (str): The path to the PDF file.

    Returns:
        bool: True if the OpenAction is a JavaScript action, False otherwise.

    Raises:
        Exception: If an error occurs while parsing the PDF's object tree.
    """
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
