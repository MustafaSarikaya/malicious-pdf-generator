from pdfalyzer.pdfalyzer import Pdfalyzer
from anytree.search import findall_by_attr


def contains_action_javascript(string1: str) -> bool:
    """
    Checks if a string contains the substring 'Action:JavaScript'.

    Parameters:
        string1 (str): The string to check.

    Returns:
        bool: True if the substring is found, False otherwise.
    """
    return 'Action:JavaScript' in string1


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
        page_nodes = findall_by_attr(pdfalyzer.pdf_tree,
                                     name='type',
                                     value='/Catalog')

        catalog_node = page_nodes[0]

        catalog_node_children = catalog_node.children[1]

        return contains_action_javascript(str(catalog_node_children))

    except Exception as e:
        print(f"Error: {e}")
        return False
