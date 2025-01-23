class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: list['HTMLNode'] = None, props: dict[str, str] = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html() not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        joined_props = ""
        for key, value in self.props.items():
            joined_props += f" {key}=\"{value}\""
        return joined_props
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props
    

    
    

    