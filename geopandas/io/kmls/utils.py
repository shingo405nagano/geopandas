import os
import random
import string
from typing import Any
from typing import Callable
from typing import List
from typing import Optional
from xml.dom import minidom
from xml.etree import ElementTree as ET

from geopandas.io.kmls.settings import SIMPLE_XMLNS
from geopandas.io.kmls.settings import Tags

IDT = " " * 4


def formatter(sentence: str, max_cols: int = 80) -> str:
    """
    ## Summary:
        Format the sentence to fit the maximum number of columns.
    Args:
        sentence(str): A sentence to format.
        max_cols(int): The maximum number of columns.
    Returns:
        str: A formatted sentence.
    """
    new_sentence = ""
    new_lines = sentence.split("\n")

    if isinstance(new_lines, str):
        new_lines = [new_lines]

    for line in new_lines:
        new_sentence += "\n"
        counter = 0
        words = line.split(" ")
        for word in words:
            if max_cols < counter + len(word):
                new_sentence += "\n"
                counter = 0
            new_sentence += word + " "
            counter += len(word) + 1
    return new_sentence.replace("\n", f"\n{IDT}")


def generate_id(length: int = 10) -> str:
    """
    ## Summary:
        Generate a random ID. This ID is used to identify the style, placemark, etc.
    Args:
        length(int):
            Length of the ID. Default is 10.
    Returns:
        str: Random ID.
    Examples:
        >>> generate_id(5)
        'X2Y4Z'
    """
    alphabet = string.ascii_uppercase
    numbers = "".join(list(map(str, list(range(10)))))
    chars = alphabet + numbers
    style_id = "".join(random.choices(chars, k=length))
    return style_id


def to_string(value: Any) -> str:
    """
    ## Summary:
        Convert value to string.
    Args:
        value(Any): Value to be converted to string.
    Returns:
        str: Converted value.
    """
    try:
        if isinstance(value, str):
            return value
        return str(value)
    except Exception as e:
        raise ValueError(f"Error converting value to string: {e}")


def to_string_decorator(arg_idx: int, kword: str):
    """
    ## Summary:
        Decorator to convert argument values to strings
    Args:
        arg_idx(int): Index of the argument to be processed by the decorator.
        kword(str): Keyword of the argument to be processed by the decorator.
    """

    def decorator(func: Callable):
        def wrapper(*args, **kwargs):
            args = list(args)
            if arg_idx < len(args):
                val = args[arg_idx]
                args[arg_idx] = to_string(val) if val else val
            if kword in kwargs:
                value = kwargs[kword]
                kwargs[kword] = to_string(value) if value else value
            return func(*args, **kwargs)

        return wrapper

    return decorator


def pretty_xml(
    element: ET.ElementTree, indent: int = 4, encoding: str = "UTF-8"
) -> str:
    """
    ## Summary:
        Convert ElementTree to pretty XML.
    Args:
        element(ET.ElementTree): ElementTree object.
        indent(int): Indent size. Default is 2.
        encoding(str): Encoding. Default is 'UTF-8'.
    Returns:
        str: Pretty XML string.
    Examples:
        >>> pretty_xml(element)
        '<?xml version="1.0" ?>\n<root>\n  <child>...</child>\n</root>'
    """
    indent = " " * indent
    xml_b = ET.tostring(element, encoding=encoding, method="xml")
    xml_str = xml_b.decode(encoding)
    parsed_xml = minidom.parseString(xml_str)
    return parsed_xml.toprettyxml(indent=indent, encoding=encoding)


def write_pretty_xml(
    file_path: str,
    element: ET.ElementTree,
    indent: int = 4,
    encoding: str = "UTF-8",
    overwrite: bool = True,
):
    """
    ## Summary:
        Write pretty XML to a file.
    Args:
        file_path(str): File path.
        element(ET.ElementTree): ElementTree object.
        indent(int): Indent size. Default is 2.
        encoding(str): Encoding. Default is 'UTF-8'.
        overwrite(bool): Overwrite the file if it already exists. Default is True.
    Raises:
        FileExistsError: If the file already exists and overwrite is False.
    """
    if overwrite == False and os.path.exists(file_path):
        raise FileExistsError(
            f"File already exists: {file_path}. Set overwrite="
            "True to overwrite the file."
        )
    xml_data = pretty_xml(element, indent, encoding)
    with open(file_path, "wb") as f:
        f.write(xml_data)


def pretty_print(element: ET.ElementTree, indent: int = 4, encoding: str = "utf-8"):
    """
    ## Summary:
        Print pretty XML. This function is useful for debugging.
    Args:
        element(ET.ElementTree): ElementTree object.
        indent(int): Indent size. Default is 4.
        encoding(str): Encoding. Default is 'utf-8'.
    """
    indent = " " * indent
    xml_str = ET.tostring(element, encoding=encoding, method="xml")
    parsed_xml = minidom.parseString(xml_str)
    print(parsed_xml.toprettyxml(indent=indent))
