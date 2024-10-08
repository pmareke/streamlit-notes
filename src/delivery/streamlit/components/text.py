import streamlit as st

from src.domain.component import Component


class Text(Component):
    def render(self, message: str) -> None:
        st.text(message)


if __name__ == "__main__":
    text = Text()
    text.render("any-text")
