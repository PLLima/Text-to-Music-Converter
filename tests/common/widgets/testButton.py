import unittest

import tkinter as tk
from PIL import Image, ImageTk
from src.common.dictionaries import BUTTON_COLORS
from src.common.widgets.button import textButton, iconButton, backButton

class testTextButton(unittest.TestCase):
    def setUp(self):
        root = tk.Tk()
        self.textButton = textButton(root, None)

    def testSetPadding(self):
        paddingX = 10
        paddingY = 10
        self.textButton.setPadding(paddingX, paddingY)
        self.assertEqual(self.textButton.getInstance().cget("padx"), paddingX, "X Padding not set accordingly.")
        self.assertEqual(self.textButton.getInstance().cget("pady"), paddingY, "Y Padding not set accordingly.")

    def testGetPadding(self):
        paddingX = 10
        paddingY = 10
        self.textButton.setPadding(paddingX, paddingY)
        self.assertEqual(self.textButton.getPaddingX(), paddingX, "X Padding not returned accordingly.")
        self.assertEqual(self.textButton.getPaddingY(), paddingY, "Y Padding not returned accordingly.")

    def testSetText(self):
        text = 'Testing...'
        fontSize = 12
        self.textButton.setText(text, fontSize)
        self.assertEqual(self.textButton.getInstance().cget("text"), text, "Text in button not set accordingly.")

    def testGetText(self):
        text = 'Testing...'
        fontSize = 12
        self.textButton.setText(text, fontSize)
        self.assertEqual(self.textButton.getText(), text, "Text in button not returned accordingly.")

    def testSetBackgroundColor(self):
        color = "Black"
        self.textButton.setBackgroundColor(BUTTON_COLORS[color])
        self.assertEqual(self.textButton.getBackgroundColor(), BUTTON_COLORS[color], "Background color not set accordingly.")
        color = "Red"
        self.textButton.setBackgroundColor(BUTTON_COLORS[color])
        self.assertEqual(self.textButton.getBackgroundColor(), BUTTON_COLORS[color], "Background color not set accordingly.")
        color = "Gray"
        self.textButton.setBackgroundColor(BUTTON_COLORS[color])
        self.assertEqual(self.textButton.getBackgroundColor(), BUTTON_COLORS[color], "Background color not set accordingly.")
        color = 'White'
        self.textButton.setBackgroundColor(color)
        self.assertNotEqual(self.textButton.getInstance().cget("bg"), color, "Undefined background color was set.")

    def testGetBackgroundColor(self):
        color = "Black"
        self.textButton.setBackgroundColor(BUTTON_COLORS[color])
        self.assertEqual(self.textButton.getBackgroundColor(), BUTTON_COLORS[color], "Background color not returned accordingly.")
        color = "Red"
        self.textButton.setBackgroundColor(BUTTON_COLORS[color])
        self.assertEqual(self.textButton.getBackgroundColor(), BUTTON_COLORS[color], "Background color not returned accordingly.")
        color = "Gray"
        self.textButton.setBackgroundColor(BUTTON_COLORS[color])
        self.assertEqual(self.textButton.getBackgroundColor(), BUTTON_COLORS[color], "Background color not returned accordingly.")
        color = 'White'
        self.textButton.setBackgroundColor(color)
        self.assertNotEqual(self.textButton.getBackgroundColor(), color, "Undefined background color was returned.")

    def testDisable(self):
        self.textButton.disable()
        self.assertEqual(self.textButton.getInstance().cget("state"), tk.DISABLED, "Button not disabled.")

    def testEnable(self):
        self.textButton.disable()
        self.textButton.enable()
        self.assertEqual(self.textButton.getInstance().cget("state"), tk.NORMAL, "Button not enabled.")

class testIconButton(unittest.TestCase):
    def setUp(self):
        root = tk.Toplevel()
        self.iconButton = iconButton(root, None)

    def testSetPadding(self):
        paddingX = 10
        paddingY = 10
        self.iconButton.setPadding(paddingX, paddingY)
        self.assertEqual(self.iconButton.getInstance().cget("padx"), paddingX, "X Padding not set accordingly.")
        self.assertEqual(self.iconButton.getInstance().cget("pady"), paddingY, "Y Padding not set accordingly.")

    def testGetPadding(self):
        paddingX = 10
        paddingY = 10
        self.iconButton.setPadding(paddingX, paddingY)
        self.assertEqual(self.iconButton.getPaddingX(), paddingX, "X Padding not returned accordingly.")
        self.assertEqual(self.iconButton.getPaddingY(), paddingY, "Y Padding not returned accordingly.")

    def testSetGetIcon(self):
        backarrow = Image.open('./src/images/backarrow.png')
        icon = ImageTk.PhotoImage(backarrow)
        self.iconButton.setIcon(icon)
        self.assertEqual(self.iconButton.getIcon(), icon, "Icon not returned accordingly.")

class testBackButton(unittest.TestCase):
    def setUp(self):
        root = tk.Tk()
        self.backButton = backButton(root, None)

    def testRender(self):
        self.backButton.getInstance().pack()
        self.backButton.getParent().update()
        self.assertTrue(self.backButton.winfo_exists(), "Back button wasn't rendered.")

if __name__ == '__main__':
    unittest.main()