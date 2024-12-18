from pylatex import Document, Center, LargeText, Figure, LineBreak
from pylatex.utils import italic, bold

def generate_card(recipient, sender, image_path="cake.jpg"):
    doc = Document(documentclass="article")

    with doc.create(Center()) as centered:
        # Line 8: No change needed here
        centered.append(LargeText(bold("Happy Birthday")))
        centered.append(LineBreak())

        with doc.create(Figure(position='h!')) as cakeimage:
            # Line 11: No change needed here
            cakeimage.add_image(image_path, width='200px')

        centered.append(LineBreak())

        # **Line 12: Corrected**
        centered.append(LargeText(["Dear ", bold(recipient), ","]))
        centered.append(LineBreak())

        # Line 14: No change needed here
        centered.append("Wishing you a day filled with love and joy")
        centered.append(LineBreak())
        centered.append(LineBreak())

        # **Line 16: Corrected**
        centered.append(italic(["From ", bold(sender)]))
        centered.append(LineBreak())

    doc.generate_pdf("BirthdayCard", compiler="pdflatex", clean_tex=False)

if __name__ == "__main__":
    recipient = input("Enter the recipient's name: ")
    sender = input("Enter the sender's name: ")
    generate_card(recipient, sender)
    print("Card generated successfully")