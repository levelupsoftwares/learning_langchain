from langchain_core.prompts import PromptTemplate

template= PromptTemplate (
    template =  """Please summarize the research paper titled {paper_input} with the following specifications:
        Explanation Style:{style_input}
        Explanation Length:{length_input}
      1.Mathematical Details:
        - Include relevent mathematical equation if present in the paper.
        - Explain the mathematical concept using simple, intituative code snippets where applicable
      2.Analogies:
        - Use relatable analogies to simplify complex ideas.
      if certain information is not avalible in the paper , respond with: "Insufficient information
      avalible" instead of guessing.
      Ensure the summary is clear , accurate, and aligned with the provided style and length.
    """,
    input_variables=['paper_input','style_input','length_input'],
    validate_template=True
)

template.save('template.json')