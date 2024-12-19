from pylatex import Document, Center, LargeText, Figure, Command, VerticalSpace
from pylatex.utils import italic, bold, NoEscape, escape_latex
from pylatex.package import Package

def generate_card(recipient, sender, image_path="cake.jpg"):
    # Escape special LaTeX characters in user inputs
    recipient_escaped = escape_latex(recipient)
    sender_escaped = escape_latex(sender)

    doc = Document(documentclass='article')
    doc.packages.append(Package('geometry',options=['paperwidth=5in','paperheight=7in']))

    doc.preamble.append(Command('pagestyle', 'empty'))

    with doc.create(Center()) as centered:
        # Add "Happy Birthday" in large bold text
        centered.append(LargeText(bold("Happy Birthday")))
        centered.append(VerticalSpace("0.5cm"))
        centered.append(Command('par'))  # Start a new paragraph

        # Add the image
        with doc.create(Figure(position='h!')) as cakeimage:
            cakeimage.add_image(image_path, width='200px')

        centered.append(Command('par'))  # Start a new paragraph
        centered.append(VerticalSpace("0.5cm"))

        # Add "Dear Recipient,"
        centered.append(LargeText(["Dear ", bold(recipient_escaped), ","]))
        centered.append(Command('par'))  # Start a new paragraph
        centered.append(VerticalSpace("0.5cm"))

        # Add the message
        centered.append("Wishing you a day filled with love and joy")
        centered.append(Command('par'))  # Start a new paragraph
        centered.append(VerticalSpace("0.5cm"))

        # Add "From Sender" in italic
        centered.append(NoEscape(r'\textit{From \textbf{' + sender_escaped + '}}'))
        centered.append(Command('par'))  # Start a new paragraph
        centered.append(VerticalSpace("0.5cm"))

    doc.generate_pdf("BirthdayCard", compiler="pdflatex", clean_tex=False)

if __name__ == "__main__":
    recipient = input("Enter the recipient's name: ")
    sender = input("Enter the sender's name: ")
    generate_card(recipient, sender)
    print("Card generated successfully")