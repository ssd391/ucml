import streamlit as st
import pandas as pd
import re
from pathlib import Path

# ----------------------
# Streamlit Configuration
# ----------------------
st.set_page_config(page_title="A11y Agent Lab", page_icon="♿️", layout="wide")

# ----------------------
# Dummy Data for Each Website
# ----------------------
# Replace these mappings with your actual JSON-loading logic
SITE_JSON_MAP = {
    "Google": [
    {
        "content": "On page https://www.google.com/ (viewport 1920-1080) we detected the following semantic violations: Violation 1 \u2014 **heading-order** (impact: moderate) \u2022 Description: Ensures the order of headings is semantically correct. \u2022 Recommendation: Heading levels should only increase by one. See https://dequeuniversity.com/rules/axe/3.5/heading-order?application=axe-puppeteer \u2022 Detail: Element \"\"\"/h3>/h3>/h3>/h3>/h3>/h3>/h3>/h3>/h3>/h3>/h3>/h3>/h3>/h3>/h3>/h3>/h3>/h3>/h3>/h3>/h3>/h3>/h3>/h3>/h3>/h3>/h3>/h3",
        "name": "semantic-agent",
        "role": "user"
    },
    {
        "content": "The a, fg: 31,31,31) and bg:255,255,255 resulting in a contrast ratio of 16.48. The a, fg: 31,31,31) and bg:255,255,255 resulting in a contrast ratio of 16.48. The a, fg: 31,31,31) and bg:255,255,255 resulting in a contrast ratio of 16.48. The a, fg: 31,31,31) and bg:255,255,255 resulting in a contrast ratio of 16.48. The a, fg:0,0 and bg:255,255,255 resulting in a contrast ratio of 21.00. The a, fg:255,255,255 bg: 11,87,208. The span element has a foreground color of RGB(255,255,255) and background color of RGB(11,87,208) resulting in a contrast ratio of 6.39. The button element has a foreground color of RGB(94,94,94) and background color of RGB(255,255,255) resulting in a contrast ratio of 6.48. The span element has a foreground color of RGB(94,94,94) and background color of RGB(255,255,255) resulting in a contrast ratio of 6.48. The span element has a foreground color of RGB(0,0,0) and background color of RGB(218,220,224) resulting in a contrast ratio of 15.29. The span element has a foreground color of RGB(0,0,0) and background color of RGB(255,255,255) resulting in a contrast ratio of 21.00. The span element has a foreground color of RGB(0,0,0) and background color of RGB(153,153,153) resulting in a contrast ratio of 7.37. The span element has a foreground color of RGB(0,0,0) and background color of RGB(153,153,153) resulting in a contrast ratio of 7.37. The span element has a foreground color of RGB(0,0,0) and background color of RGB(255,255,255) resulting in a contrast ratio of 21.00. The span element has a foreground color of RGB(112,117,122) and background color of RGB(255,255,255) resulting in a contrast ratio of 4.65. The span element has a foreground color of RGB(0,0,0) and background color of RGB(255,255,255) resulting in a contrast ratio of 21.00. The span element has a foreground color of RGB(154,160,166) and background color of RGB(255,255,255) resulting in a contrast ratio of 2.64. This is below the WCAG recommended minimum of 4.5:1 for normal text. The span element has a foreground color of RGB(94,94,94) and background color of RGB(255,255,255) resulting in a contrast ratio of 6.48. The span element has a foreground color of RGB(31,31,31) and background color of RGB(255,255,255) resulting in a contrast ratio of 16.48. The span element has a foreground color of RGB(255,255,255) and background color of RGB(11,87,208) resulting in a contrast ratio of 6.39. The li element has a foreground color of RGB(31,31,31) and background color of RGB(255,255,255) resulting in a contrast ratio of 16.48. The span element has a foreground color of RGB(33,33,33) and background color of RGB(255,255,255) resulting in a contrast ratio of 16.10. The span element has a foreground color of RGB(112,117,122) and background color of RGB(255,255,255) resulting in a contrast ratio of 4.65. The span element has a foreground color of RGB(31,31,31) and background color of RGB(255,255,255) resulting in a contrast ratio of 16.48. The span element has a foreground color of RGB(32,33,36) and background color of RGB(255,255,255) resulting in a contrast ratio of 16.10. The span element has a foreground color of RGB(94,94,94) and background color of RGB(255,255,255) resulting in a contrast ratio of 6.48. The li element has a foreground color of RGB(31,31,31) and background color of RGB(255,255,255) resulting in a contrast ratio of 16.48. The span element has a foreground color of RGB(94,94,94) and background color of RGB(255,255,255) resulting in a contrast ratio of 6.48. The span element has a foreground color of RGB(31,31,31) and background color of RGB(255,255,255) resulting in a contrast ratio of 16.48. The li element has a foreground color of RGB(31,31,31) and background color of RGB(255,255,255) resulting in a contrast ratio of 16.48. The span element has a foreground color of RGB(33,33,33) and background color of RGB(255,255,255) resulting in a contrast ratio of 16.10. The span element has a foreground color of RGB(112,117,122) and background color of RGB(255,255,255) resulting in a contrast ratio of 4.65. The span element has a foreground color of RGB(94,94,94) and background color of RGB(255,255,255) resulting in a contrast ratio of 6.48. The span element has a foreground color of RGB(31,31,31) and background color of RGB(255,255,255) resulting in a contrast ratio of 16.48. The li element has a foreground color of RGB(31,31,31) and background color of RGB(255,255,255) resulting in a contrast ratio of 16.48. The span element has a foreground color of RGB(31,31,31) and background color of RGB(255,255,255) resulting in a contrast ratio of 16.48. The span element has a foreground color of RGB(112,117,122) and background color of RGB(255,255,255) resulting in a contrast ratio of 4.65. The span element has a foreground color of RGB(60,64,67) and background color of RGB(248,249,250) resulting in a contrast ratio of 9.93. The span element has a foreground color of RGB(60,64,67) and background color of RGB(248,249,250) resulting in a contrast ratio of 9.93. The span element has a foreground color of RGB(60,64,67) and background color of RGB(248,249,250) resulting in a contrast ratio of 9.93. The span element has a foreground color of RGB(60,64,67) and background color of RGB(248,249,250) resulting in a contrast ratio of 9.93. The span element has a foreground color of RGB(60,64,67) and background color of RGB(248,249,250) resulting in a contrast ratio of 9.93. The span element has a foreground color of RGB(60,64,67) and background color of RGB(248,249,250) resulting in a contrast ratio of 9.93. The span element has a foreground color of RGB(60,64,67) and background color of RGB(248,249,250) resulting in a contrast ratio of 9.93. The span element has a foreground color of RGB(60,64,67) and background color of RGB(248,249,250) resulting in a contrast ratio of 9.93. The span element has a foreground color of RGB(60,64,67) and background color of RGB(248,249,250) resulting in a contrast ratio of 9.93. The a, fg: 31,31,31) and bg: 242,242,242) resulting in a contrast ratio of 14.72. The a, fg: 31,31,31) and bg: 242,242,242) resulting in a contrast ratio of 14.72. The a, fg: 31,31,31) and bg: 242,242,242) resulting in a contrast ratio of 14.72. The a, fg: 31,31,31) and bg: 242,242,242) resulting in a contrast ratio of 14.72. The span element has a foreground color of RGB(31,31,31) and background color of RGB(242,242,242) resulting in a contrast ratio of 14.72. The a, fg: 31,31,31) and bg: 242,242,242) resulting in a contrast ratio of 14.72. The a, fg: 31,31,31) and bg: 242,242,242) resulting in a contrast ratio of 14.72. The span element has a foreground color of RGB(31,31,31) and background color of RGB(242,242,242) resulting in a contrast ratio of 14.72. The span element has a foreground color of RGB(31,31,31) and background color of RGB(242,242,242) resulting in a contrast ratio of 14.72. The a, fg: 31,31,31) and bg:255,255,255 resulting in a contrast ratio of 16.48. The a, fg: 31,31,31) and bg:255,255,255 resulting in a contrast ratio of 16.48. The a, fg: 31,31,31) and bg:255,255,255 resulting in a contrast ratio of 16.48. The a, fg: 31,31,31) and bg:255,255,255 resulting in a contrast ratio of 16.48. The a, fg: 31,31,31) and bg:255,255,255 resulting in a contrast ratio of 16.48. The span element has a foreground color of RGB(31,31,31) and background color of RGB(255,255,255) resulting in a contrast ratio of 16.48. The span element has a foreground color of RGB(94,94,94) and background color of RGB(255,255,255) resulting in a contrast ratio of 6.48. The span element has a foreground color of RGB(31,31,31) and background color of RGB(255,255,255) resulting in a contrast ratio of 16.48. The span element has a foreground color of RGB(31,31,31) and background color of RGB(255,255,255) resulting in a contrast ratio of 16.48.",
        "name": "contrast-agent",
        "role": "user"
    },
    {
        "content": "- aria-allowed-role (impact: minor)\n    Categories: cat.aria\n    Description: Ensure role attribute has an appropriate value for the element\n    Help: ARIA role should be appropriate for the element\n    FailureSummary: Fix any of the following:; ARIA role combobox is not allowed for given element\n- landmark-one-main (impact: moderate)\n    Categories: cat.semantics\n    Description: Ensure the document has a main landmark\n    Help: Document should have one main landmark\n    FailureSummary: Fix all of the following:; Document does not have a main landmark\n- page-has-heading-one (impact: moderate)\n    Categories: cat.semantics\n    Description: Ensure that the page, or at least one of its frames contains a level-one heading\n    Help: Page should contain a level-one heading\n    FailureSummary: Fix all of the following:; Page must have a level-one heading",
        "name": "axe-violations-agent",
        "role": "user"
    },
    {
        "content": "For nodeId img-9, the alt text is missing and the generated caption is 'a green leaf with a white background'. For nodeId svg-0, the alt text is missing and the generated caption is 'a white background with black circles'. For nodeId svg-1, the alt text is missing and the generated caption is 'google logo'. For nodeId svg-3, the alt text is missing and the generated caption is 'a black and white photo of a magni'. For nodeId svg-5, the alt text is missing and the generated caption is 'a microphone icon'. For nodeId svg-6, the alt text is missing and the generated caption is 'the logo for the new line of products'.",
        "name": "image-captioning-agent",
        "role": "user"
    },
    {
        "content": "The SemanticAgent has identified a violation in the heading order on the page. The heading levels should increase by one, but this is not the case on the page. This could make it difficult for screen reader users to understand the structure of the content.\n\nThe ContrastAgent has identified several elements on the page with good contrast ratios, which is beneficial for users with visual impairments. However, there is one span element with a foreground color of RGB(154,160,166) and background color of RGB(255,255,255) resulting in a contrast ratio of 2.64, which is below the WCAG recommended minimum of 4.5:1 for normal text. This could make the text difficult to read for some users.\n\nThe AxeViolationsAgent has identified three violations. The first is a minor impact violation related to the ARIA role attribute not having an appropriate value for the element. The second is a moderate impact violation due to the document not having a main landmark. The third is also a moderate impact violation because the page does not contain a level-one heading. These violations could make it difficult for screen reader users to navigate and understand the page.\n\nThe ImageCaptioningAgent has identified several images on the page that are missing alt text. Alt text is important for screen reader users as it provides a description of the image content. The agent has provided generated captions for these images, but it would be better if appropriate alt text was added to the images.",
        "name": "VisuallyImpairedAgent",
        "role": "user"
    },
    {
        "content": "The page structure presents several barriers for keyboard-only users:\n\n1. **Semantic Violations**: The incorrect order of headings can make it difficult for keyboard-only users to navigate the page using heading levels. This is especially problematic for users who rely on screen readers, as they often use headings to understand the page structure.\n\n2. **Contrast Issues**: While most elements on the page have good contrast ratios, there is a span element with a contrast ratio below the WCAG recommended minimum. This could make it difficult for users with visual impairments to read the text, especially if they are navigating the page using a keyboard and cannot easily zoom in or adjust the display.\n\n3. **ARIA Role Violations**: The inappropriate ARIA role attribute can confuse screen reader users, making it difficult for them to understand the purpose of the element and how to interact with it using a keyboard.\n\n4. **Missing Main Landmark**: The absence of a main landmark can make it difficult for keyboard-only users to navigate the page, as they cannot easily jump to the main content.\n\n5. **Missing Level-One Heading**: The absence of a level-one heading can make it difficult for keyboard-only users to understand the overall structure of the page, as they cannot easily identify the main topic or purpose of the page.\n\n6. **Missing Alt Text**: The missing alt text for several images can make it difficult for keyboard-only users who rely on screen readers to understand the content of the images. While the generated captions provide some information, they may not fully convey the purpose or content of the images in the context of the page.\n\nIn summary, to improve keyboard navigation, the page should correct the heading order, improve the contrast ratio of the low-contrast span element, use appropriate ARIA roles, include a main landmark, add a level-one heading, and provide meaningful alt text for all images.",
        "name": "MotorImpairedAgent",
        "role": "user"
    },
    {
        "content": "The SemanticAgent has identified a violation in the heading order on the page. The heading levels should increase by one, but this is not the case on the page. This could make it difficult for screen reader users to understand the structure of the content.\n\nThe ContrastAgent has identified several elements on the page with good contrast ratios, which is beneficial for users with visual impairments. However, there is one span element with a foreground color of RGB(154,160,166) and background color of RGB(255,255,255) resulting in a contrast ratio of 2.64, which is below the WCAG recommended minimum of 4.5:1 for normal text. This could make the text difficult to read for some users.\n\nThe AxeViolationsAgent has identified three violations. The first is a minor impact violation related to the ARIA role attribute not having an appropriate value for the element. The second is a moderate impact violation due to the document not having a main landmark. The third is also a moderate impact violation because the page does not contain a level-one heading. These violations could make it difficult for screen reader users to navigate and understand the page.\n\nThe ImageCaptioningAgent has identified several images on the page that are missing alt text. Alt text is important for screen reader users as it provides a description of the image content. The agent has provided generated captions for these images, but it would be better if appropriate alt text was added to the images.",
        "name": "ColorBlindAgent",
        "role": "user"
    },
    {
        "content": "1. **Semantic Violation (SemanticAgent)**: The heading order on the page is incorrect. The heading levels should increase by one. This can be fixed by adjusting the heading levels to ensure they increase sequentially. For example, if a `<h2>` is followed by a `<h4>`, the `<h4>` should be changed to a `<h3>`.\n\n    ```html\n    <h1>...</h1>\n    <h2>...</h2>\n    <h3>...</h3>\n    <!-- and so on -->\n    ```\n\n2. **Contrast Issues (ContrastAgent)**: There is a span element with a contrast ratio below the WCAG recommended minimum. This can be fixed by adjusting the color of the text or the background to increase the contrast ratio. For example:\n\n    ```css\n    span {\n        color: #000000; /* or any other color with sufficient contrast */\n    }\n    ```\n\n3. **ARIA Role Violations (AxeViolationsAgent)**: An inappropriate ARIA role attribute is being used. This can be fixed by changing the role attribute to an appropriate value for the element. For example, if a `div` element is being used as a button, it should have a role of \"button\".\n\n    ```html\n    <div role=\"button\">...</div>\n    ```\n\n4. **Missing Main Landmark (AxeViolationsAgent)**: The document does not have a main landmark. This can be fixed by adding a `<main>` element to wrap the main content of the page.\n\n    ```html\n    <main>\n        <!-- main content goes here -->\n    </main>\n    ```\n\n5. **Missing Level-One Heading (AxeViolationsAgent)**: The page does not contain a level-one heading. This can be fixed by adding a `<h1>` element to the page.\n\n    ```html\n    <h1>Page Title</h1>\n    ```\n\n6. **Missing Alt Text (ImageCaptioningAgent)**: Several images on the page are missing alt text. This can be fixed by adding an `alt` attribute to each `img` element. The value of the `alt` attribute should describe the content of the image.\n\n    ```html\n    <img src=\"image.jpg\" alt=\"description of image\">\n    ```",
        "name": "FixingAgent",
        "role": "user"
    }
],
    "Microsoft": [
    {
        "content": "On page https://www.microsoft.com/en-us/ (viewport 1920-1080) we detected the following semantic violations: Violation 1 \u2014 **heading-order** (impact: moderate) \u2022 Description: Ensures the order of headings is semantically correct. \u2022 Recommendation: Heading levels should only increase by one. See https://dequeuniversity.com/rules/axe/3.5/heading-order?application=axe-puppeteer \u2022 Detail: Element \"\">Surface Pro, Copilot+ PC with a keyboard attached./h3>/h3>/h3>/h3>/h3>/h3>/h3>/h3>/h3>/h3>/h3>/h3>/h3>/h3>/h3>/h3>/h3>/h3>/h3>/h3>/h3>/h3>/h3>/h3>/",
        "name": "semantic-agent",
        "role": "user"
    },
    {
        "content": "The a, fg:255,255,255 bg:255,255 resulting in a contrast ratio of 1.00. This is below the WCAG recommended minimum of 4.5:1 for normal text. The a, fg:255,255,255 bg:255,255 resulting in a contrast ratio of 1.00. This is below the WCAG recommended minimum of 4.5:1 for normal text. The a, fg:255,255,255 bg:255,255 resulting in a contrast ratio of 1.00. This is below the WCAG recommended minimum of 4.5:1 for normal text. The a, fg:255,255,255 bg:255,255 resulting in a contrast ratio of 1.00. This is below the WCAG recommended minimum of 4.5:1 for normal text. The button element has a foreground color of RGB(255,255,255) and background color of RGB(255,255,255) resulting in a contrast ratio of 1.00. This is below the WCAG recommended minimum of 4.5:1 for normal text. The button element has a foreground color of RGB(255,255,255) and background color of RGB(255,255,255) resulting in a contrast ratio of 1.00. This is below the WCAG recommended minimum of 4.5:1 for normal text. The role has a foreground color of RGB(255,255,255) and background color of RGB(255,255,255) resulting in a contrast ratio of 1.00. This is below the WCAG recommended minimum of 4.5:1 for normal text. The p, fg:255,255,255 bg:255,255 resulting in a contrast ratio of 1.00. This is below the WCAG recommended minimum of 4.5:1 for normal text. The role has a foreground color of RGB(255,255,255) and background color of RGB(255,255,255) resulting in a contrast ratio of 1.00. This is below the WCAG recommended minimum of 4.5:1 for normal text.",
        "name": "contrast-agent",
        "role": "user"
    },
    {
        "content": "- landmark-unique (impact: moderate)\n    Categories: cat.semantics\n    Description: Ensure landmarks are unique\n    Help: Landmarks should have a unique role or role/label/title (i.e. accessible name) combination\n    FailureSummary: Fix any of the following:; The landmark must have a unique aria-label, aria-labelledby, or title to make landmarks distinguishable\n- region (impact: moderate)\n    Categories: cat.keyboard\n    Description: Ensure all page content is contained by landmarks\n    Help: All page content should be contained by landmarks\n    FailureSummary: Fix any of the following:; Some page content is not contained by landmarks",
        "name": "axe-violations-agent",
        "role": "user"
    },
    {
        "content": "For nodeId img-0, the alt text is missing and the generated caption is 'microsoft logo'. For nodeId img-1, the alt image text is 'Copilot+ PC logo.', and the generated caption is 'the logo of the company'. For nodeId img-2, the alt image text is 'A collection of multiple Surface, Copilot+ PC devices.', and the generated caption is 'apple mac pro 13'. For nodeId img-3, the alt image text is 'Surface Pro, Copilot+ PC with a keyboard attached.', and the generated caption is 'the ipad keyboard with keyboard keyboard'. For nodeId img-4, the alt image text is 'A front facing Surface Laptop, Copilot+ PC.', and the generated caption is 'apple mac mac 13 re re re re re re re re re re re re re re re re re'. For nodeId img-5, the alt image text is 'Mouse and Dock accessories for Surface devices', and the generated caption is 'a purple mouse and a black mouse mouse'. For nodeId img-6, the alt text is missing and the generated caption is 'a laptop computer with a blank screen'. For nodeId img-7, the alt text is missing and the generated caption is 'the logo of the university of north carolina'. For nodeId img-8, the alt text is missing and the generated caption is 'a computer with a clock on it'. For nodeId img-9, the alt text is missing and the generated caption is 'a black and white suitcase'. For nodeId img-10, the alt text is missing and the generated caption is 'a computer monitor icon'. For nodeId img-11, the alt text is missing and the generated caption is 'the logo for the new line of clothing'. For nodeId img-12, the alt image text is 'Microsoft 365 suite of apps such as Teams, Word, Outlook, and more.', and the generated caption is 'a laptop with a bunch of colorful letters on it'. For nodeId img-13, the alt image text is 'Red, white, blue, and black Xbox Wireless Controllers', and the generated caption is 'xbox gamepads are coming in the us'. For nodeId img-14, the alt image text is 'An Xbox Series S console and an Xbox controller', and the generated caption is 'the xbox game console is shown in this image'. For nodeId img-15, the alt image text is 'A variety of games available with Xbox Game Pass.', and the generated caption is 'the game pass logo with a bunch of video games'. For nodeId img-16, the alt image text is 'Three screenshots from the Copilot App', and the generated caption is 'the app for the app store, which features a variety of apps'. For nodeId img-17, the alt image text is 'A Surface Laptop for Business in the color Platinum and Surface Pro for Business with a Surface Pro Flex Keyboard in the color Black.', and the generated caption is 'apple macbook pro 13'. For nodeId img-18, the alt image text is 'A Surface Pro for Business, Copilot+ PC, 12-inch | Snapdragon and a Surface Laptop for Business, Copilot+ PC, 13-inch | Snapdragon in the color Platinum.', and the generated caption is 'apple macbook pro 13'. For nodeId img-19, the alt image text is 'Visual Studio Icon.', and the generated caption is 'the logo for the new xiao phone'. For nodeId img-20, the alt image text is 'A laptop running Windows 11.', and the generated caption is 'a laptop with a blue rose on the screen'. For nodeId img-21, the alt image text is 'collaged illustration of a woman running up an escalator surrounded by stylized charts.', and the generated caption is 'a man is sitting on a blue and yellow graphic'. For nodeId img-22, the alt image text is 'Azeem Azhar.', and the generated caption is 'a man in a suit and glasses smiles while he stands in front of a colorful background'. For nodeId img-23, the alt image text is 'Musician Cuco looks up at an animated version of himself skateboarding down a street in LA.', and the generated caption is 'a man sitting on a red car in front of a palm tree'. For nodeId img-25, the alt image text is 'A blueprint for a fantastical building created with AI.', and the generated caption is 'a man and woman standing next to each other people'. For nodeId img-26, the alt image text is 'Facebook', and the generated caption is 'the facebook logo'. For nodeId img-27, the alt image text is 'X', and the generated caption is 'the x logo'. For nodeId img-28, the alt image text is 'LinkedIn', and the generated caption is 'the logo for the social network'. For nodeId img-30, the alt image text is 'Need Help? Lets Chat', and the generated caption is 'a black background with a white and red flower'. For nodeId img-31, the alt image text is 'Need Help? Lets Chat', and the generated caption is 'a woman with a blue background and a white background with the words, what is the future of the internet'. For nodeId svg-0, the alt text is missing and the generated caption is 'the logo for the vm'.",
        "name": "image-captioning-agent",
        "role": "user"
    },
    {
        "content": "The analysis reveals several accessibility issues on the page. \n\nFrom the SemanticAgent, there is a violation in the heading order. The heading levels should increase by one, but it seems there are multiple h3 headings following each other, which is not semantically correct. This could make it difficult for screen reader users to understand the structure of the content.\n\nThe ContrastAgent has identified multiple contrast issues. The color contrast between the foreground and background for several elements, including links (a), buttons, and paragraphs (p), is 1.00, which is significantly below the WCAG recommended minimum of 4.5:1 for normal text. This could make the text hard to read for users with low vision or color vision deficiencies.\n\nThe AxeViolationsAgent has detected two violations. The first is that landmarks are not unique, which could make it difficult for screen reader users to distinguish between different sections of the page. The second violation is that some page content is not contained by landmarks, which could make it difficult for keyboard-only users to navigate the page.\n\nThe ImageCaptioningAgent has identified several images where the alt text is missing. This could make it difficult for screen reader users to understand the content of these images. Additionally, there are several instances where the generated caption does not match the alt text, which could indicate that the alt text is not accurately describing the image. For example, for nodeId img-2, the alt text is 'A collection of multiple Surface, Copilot+ PC devices.', but the generated caption is 'apple mac pro 13'. \n\nIn conclusion, the page has several accessibility issues that need to be addressed to improve the experience for all users, particularly those using assistive technologies.",
        "name": "VisuallyImpairedAgent",
        "role": "user"
    },
    {
        "content": "The analysis reveals several accessibility issues on the page. \n\nFrom the SemanticAgent, there is a violation in the heading order. The heading levels should increase by one, but it seems there are multiple h3 headings following each other, which is not semantically correct. This could make it difficult for screen reader users to understand the structure of the content.\n\nThe ContrastAgent has identified multiple contrast issues. The color contrast between the foreground and background for several elements, including links (a), buttons, and paragraphs (p), is 1.00, which is significantly below the WCAG recommended minimum of 4.5:1 for normal text. This could make the text hard to read for users with low vision or color vision deficiencies.\n\nThe AxeViolationsAgent has detected two violations. The first is that landmarks are not unique, which could make it difficult for screen reader users to distinguish between different sections of the page. The second violation is that some page content is not contained by landmarks, which could make it difficult for keyboard-only users to navigate the page.\n\nThe ImageCaptioningAgent has identified several images where the alt text is missing. This could make it difficult for screen reader users to understand the content of these images. Additionally, there are several instances where the generated caption does not match the alt text, which could indicate that the alt text is not accurately describing the image. For example, for nodeId img-2, the alt text is 'A collection of multiple Surface, Copilot+ PC devices.', but the generated caption is 'apple mac pro 13'. \n\nIn conclusion, the page has several accessibility issues that need to be addressed to improve the experience for all users, particularly those using assistive technologies.",
        "name": "MotorImpairedAgent",
        "role": "user"
    },
    {
        "content": "The analysis reveals several accessibility issues on the page. \n\nFrom the SemanticAgent, there is a violation in the heading order. The heading levels should increase by one, but it seems there are multiple h3 headings following each other, which is not semantically correct. This could make it difficult for screen reader users to understand the structure of the content.\n\nThe ContrastAgent has identified multiple contrast issues. The color contrast between the foreground and background for several elements, including links (a), buttons, and paragraphs (p), is 1.00, which is significantly below the WCAG recommended minimum of 4.5:1 for normal text. This could make the text hard to read for users with low vision or color vision deficiencies.\n\nThe AxeViolationsAgent has detected two violations. The first is that landmarks are not unique, which could make it difficult for screen reader users to distinguish between different sections of the page. The second violation is that some page content is not contained by landmarks, which could make it difficult for keyboard-only users to navigate the page.\n\nThe ImageCaptioningAgent has identified several images where the alt text is missing. This could make it difficult for screen reader users to understand the content of these images. Additionally, there are several instances where the generated caption does not match the alt text, which could indicate that the alt text is not accurately describing the image. For example, for nodeId img-2, the alt text is 'A collection of multiple Surface, Copilot+ PC devices.', but the generated caption is 'apple mac pro 13'. \n\nIn conclusion, the page has several accessibility issues that need to be addressed to improve the experience for all users, particularly those using assistive technologies.",
        "name": "ColorBlindAgent",
        "role": "user"
    },
    {
        "content": "1. Issue: Incorrect heading order (SemanticAgent)\n   Fix: Ensure that heading levels only increase by one. For example, if you have an h2 heading, the next heading should be h3, not h4 or h5.\n   ```html\n   <h2>Heading level 2</h2>\n   <h3>Heading level 3</h3>\n   ```\n\n2. Issue: Low contrast ratio (ContrastAgent)\n   Fix: Adjust the color of the text and/or the background to meet the WCAG recommended minimum contrast ratio of 4.5:1 for normal text.\n   ```css\n   a, button, p, .role {\n       color: #000000; /* Adjust as needed */\n       background-color: #FFFFFF; /* Adjust as needed */\n   }\n   ```\n\n3. Issue: Non-unique landmarks (AxeViolationsAgent)\n   Fix: Ensure that landmarks have a unique role or role/label/title combination. This can be achieved by using the `aria-label`, `aria-labelledby`, or `title` attributes.\n   ```html\n   <nav aria-label=\"Primary navigation\"></nav>\n   <nav aria-label=\"Secondary navigation\"></nav>\n   ```\n\n4. Issue: Page content not contained by landmarks (AxeViolationsAgent)\n   Fix: Ensure that all page content is contained within landmarks. This can be achieved by wrapping content in landmark elements such as `<main>`, `<header>`, `<footer>`, `<nav>`, `<aside>`, etc.\n   ```html\n   <main>\n       <!-- Page content goes here -->\n   </main>\n   ```\n\n5. Issue: Missing alt text for images (ImageCaptioningAgent)\n   Fix: Add alt text to images to describe the content of the image. This can be achieved by using the `alt` attribute.\n   ```html\n   <img src=\"image.jpg\" alt=\"Description of image\">\n   ```\n\n6. Issue: Mismatch between alt text and generated caption (ImageCaptioningAgent)\n   Fix: Ensure that the alt text accurately describes the content of the image. If the generated caption does not match the alt text, consider updating the alt text to more accurately reflect the image content.\n   ```html\n   <img src=\"image.jpg\" alt=\"Updated description of image\">\n   ```",
        "name": "FixingAgent",
        "role": "user"
    }
],
 "GNU" : [
    {
        "content": "On page https://www.gnu.org/ (viewport 1920-1080) we detected the following semantic violations: Violation 1 \u2014 **heading-order** (impact: moderate) \u2022 Description: Ensures the order of headings is semantically correct. \u2022 Recommendation: Heading levels should only increase by one. See https://dequeuniversity.com/rules/axe/3.5/heading-order?application=axe-puppeteer \u2022 Detail: Element \"\">What is GNU?/h4>/h4>/h4>/h4>/h4>/h4>/h4>/h4>/h4>/h4>/h4>/h4>/h4>/h4>/h4>/h4>/h4>/h4>/h4>/h4>/h4>/h4>/h4>/h4>/h4>/h4>/h4",
        "name": "semantic-agent",
        "role": "user"
    },
    {
        "content": "The li element has a foreground color of RGB(34,34,34) and background color of RGB(163,45,42) resulting in a contrast ratio of 2.25. This is below the WCAG recommended minimum of 4.5:1 for normal text. The li element has a foreground color of RGB(34,34,34) and background color of RGB(163,45,42) resulting in a contrast ratio of 2.25. This is below the WCAG recommended minimum of 4.5:1 for normal text. The li element has a foreground color of RGB(34,34,34) and background color of RGB(163,45,42) resulting in a contrast ratio of 2.25. This is below the WCAG recommended minimum of 4.5:1 for normal text. The li element has a foreground color of RGB(34,34,34) and background color of RGB(163,45,42) resulting in a contrast ratio of 2.25. This is below the WCAG recommended minimum of 4.5:1 for normal text. The li element has a foreground color of RGB(34,34,34) and background color of RGB(163,45,42) resulting in a contrast ratio of 2.25. This is below the WCAG recommended minimum of 4.5:1 for normal text. The li element has a foreground color of RGB(34,34,34) and background color of RGB(163,45,42) resulting in a contrast ratio of 2.25. This is below the WCAG recommended minimum of 4.5:1 for normal text. The li element has a foreground color of RGB(34,34,34) and background color of RGB(163,45,42) resulting in a contrast ratio of 2.25. This is below the WCAG recommended minimum of 4.5:1 for normal text. The li element has a foreground color of RGB(34,34,34) and background color of RGB(163,45,42) resulting in a contrast ratio of 2.25. This is below the WCAG recommended minimum of 4.5:1 for normal text. The li element has a foreground color of RGB(34,34,34) and background color of RGB(163,45,42) resulting in a contrast ratio of 2.25. This is below the WCAG recommended minimum of 4.5:1 for normal text. The li element has a foreground color of RGB(34,34,34) and background color of RGB(163,45,42) resulting in a contrast ratio of 2.25. This is below the WCAG recommended minimum of 4.5:1 for normal text. The li element has a foreground color of RGB(34,34,34) and background color of RGB(163,45,42) resulting in a contrast ratio of 2.25. This is below the WCAG recommended minimum of 4.5:1 for normal text. The li element has a foreground color of RGB(34,34,34) and background color of RGB(163,45,42) resulting in a contrast ratio of 2.25. This is below the WCAG recommended minimum of 4.5:1 for normal text. The li element has a foreground color of RGB(34,34,34) and background color of RGB(163,45,42) resulting in a contrast ratio of 2.25. This is below the WCAG recommended minimum of 4.5:1 for normal text. The li element has a foreground color of RGB(34,34,34) and background color of RGB(163,45,42) resulting in a contrast ratio of 2.25. This is below the WCAG recommended minimum of 4.5:1 for normal text. The li element has a foreground color of RGB(34,34,34) and background color of RGB(163,45,42) resulting in a contrast ratio of 2.25. This is below the WCAG recommended minimum of 4.5:1 for normal text. The li element has a foreground color of RGB(34,34,34) and background color of RGB(163,45,42) resulting in a contrast ratio of 2.25. This is below the WCAG recommended minimum of 4.5:1 for normal text.",
        "name": "contrast-agent",
        "role": "user"
    },
    {
        "content": "- landmark-unique (impact: moderate)\n    Categories: cat.semantics\n    Description: Ensure landmarks are unique\n    Help: Landmarks should have a unique role or role/label/title (i.e. accessible name) combination\n    FailureSummary: Fix any of the following:; The landmark must have a unique aria-label, aria-labelledby, or title to make landmarks distinguishable\n- page-has-heading-one (impact: moderate)\n    Categories: cat.semantics\n    Description: Ensure that the page, or at least one of its frames contains a level-one heading\n    Help: Page should contain a level-one heading\n    FailureSummary: Fix all of the following:; Page must have a level-one heading\n- region (impact: moderate)\n    Categories: cat.keyboard\n    Description: Ensure all page content is contained by landmarks\n    Help: All page content should be contained by landmarks\n    FailureSummary: Fix any of the following:; Some page content is not contained by landmarks",
        "name": "axe-violations-agent",
        "role": "user"
    },
    {
        "content": "For nodeId img-0, the alt image text is '\u00a0[A GNU head]\u00a0', and the generated caption is 'a black and white drawing of a ram'. For nodeId img-1, the alt image text is '\u00a0[Search www.gnu.org]\u00a0', and the generated caption is 'a magnized black and white image of a magnized black and white image of a magnized black and white'. For nodeId img-2, the alt image text is '\u00a0[Other languages]\u00a0', and the generated caption is 'the logo for the american academy'. For nodeId img-3, the alt image text is '\u00a0[Screenshot of Dragora\u00a03.0-beta2 with TDE desktop]\u00a0', and the generated caption is 'a computer screen with a blue background'. For nodeId img-4, the alt image text is '\u00a0[Screenshot of Dragora\u00a03.0-beta2 with TDE desktop]\u00a0', and the generated caption is 'a computer screen with a picture of a shark'. For nodeId img-5, the alt image text is '\u00a0[Screenshot of Guix\u00a00.15 with GNOME\u00a03 desktop]\u00a0', and the generated caption is 'the website of the new york school of medicine'. For nodeId img-6, the alt image text is '\u00a0[Screenshot of Hyperbola\u00a00.3 with i3 window manager]\u00a0', and the generated caption is 'a laptop with a screen showing a page'. For nodeId img-7, the alt image text is '\u00a0[Screenshot of Parabola\u00a02020 with LXDE desktop]\u00a0', and the generated caption is 'the screen is showing the logo for the company'. For nodeId img-8, the alt image text is '\u00a0[Screenshot of PureOS\u00a08 with GNOME\u00a03 desktop]\u00a0', and the generated caption is 'a laptop with a screen showing a picture of a dog'. For nodeId img-9, the alt image text is '\u00a0[Screenshot of Trisquel\u00a010 with MATE desktop]\u00a0', and the generated caption is 'the windows phone app'. For nodeId img-10, the alt image text is 'Help people bypass censorship. Run Snowflake!', and the generated caption is 'the logo for the hype byaspher'. For nodeId img-11, the alt image text is 'RSS Feed', and the generated caption is 'a bottle of beer with a white label'. For nodeId img-12, the alt image text is 'logo for bpel2owfn', and the generated caption is 'the logo for the new apple company'. For nodeId img-13, the alt image text is '\u00a0[FSF logo]\u00a0', and the generated caption is 'the logo for the new logo for the new business'.",
        "name": "image-captioning-agent",
        "role": "user"
    },
    {
        "content": "The SemanticAgent has identified a violation in the heading order on the page. The heading \"What is GNU?\" is marked as an h4, which may not follow a semantically correct order of headings. Headings should increase by only one level at a time, so this should be corrected to improve the page's accessibility.\n\nThe ContrastAgent has found that the contrast ratio of the text within the li elements is below the recommended minimum. The foreground color of RGB(34,34,34) and background color of RGB(163,45,42) results in a contrast ratio of 2.25, which is below the WCAG recommended minimum of 4.5:1 for normal text. This could make the text difficult to read for users with visual impairments and should be adjusted to meet the recommended contrast ratio.\n\nThe AxeViolationsAgent has identified several issues. The page lacks a level-one heading, which is important for providing a clear structure. Additionally, some content is not contained by landmarks, which can make navigation difficult for screen reader users. Lastly, landmarks on the page are not unique, which can also cause confusion during navigation.\n\nThe ImageCaptioningAgent has provided alternative text and generated captions for several images on the page. Some of the generated captions do not seem to accurately describe the images based on their alternative text. For example, the image with alt text '\u00a0[Screenshot of Dragora\u00a03.0-beta2 with TDE desktop]\u00a0' has a generated caption of 'a computer screen with a picture of a shark', which may not be accurate. It's important to ensure that alternative text accurately describes the content of images for users who cannot see them.",
        "name": "VisuallyImpairedAgent",
        "role": "user"
    },
    {
        "content": "Based on the combined accessibility summary, the following keyboard navigation barriers are identified:\n\n1. **Heading Order**: The page has a semantic violation in the heading order. The heading \"What is GNU?\" is marked as an h4, which may not follow a semantically correct order of headings. This could confuse keyboard-only users who rely on headings for navigation.\n\n2. **Contrast Ratio**: The contrast ratio of the text within the li elements is below the recommended minimum. This could make the text difficult to read for users with visual impairments and could also affect users who rely on high contrast settings for better visibility.\n\n3. **Landmarks**: The page lacks unique landmarks and some content is not contained by landmarks. This could make navigation difficult for keyboard-only users who rely on landmarks to understand the structure of the page and to navigate through it.\n\n4. **Missing Level-One Heading**: The page lacks a level-one heading. This is a barrier for keyboard navigation as users often rely on this primary heading to understand the main content of the page.\n\n5. **Image Alternative Text**: Some of the generated captions do not seem to accurately describe the images based on their alternative text. This could confuse users who rely on screen readers and cannot see the images.\n\nTo improve keyboard navigation, the page should correct the heading order, adjust the contrast ratio of text, ensure all content is contained by unique landmarks, include a level-one heading, and provide accurate alternative text for images.",
        "name": "MotorImpairedAgent",
        "role": "user"
    },
    {
        "content": "As a color-blind user, the reported contrast ratio of 2.25:1 for the li elements is a significant issue. This ratio is below the WCAG recommended minimum of 4.5:1 for normal text, which means I may have difficulty distinguishing the text from its background. The semantic issues reported, such as the incorrect heading order and lack of unique landmarks, do not directly relate to color blindness, but they do affect the overall accessibility of the page.",
        "name": "ColorBlindAgent",
        "role": "user"
    },
    {
        "content": "Based on the findings from the SemanticAgent, ContrastAgent, AxeViolationsAgent, ImageCaptioningAgent, VisuallyImpairedAgent, MotorImpairedAgent, and ColorBlindAgent, the following code-level fixes are recommended:\n\n1. **Heading Order Violation** (SemanticAgent): The heading \"What is GNU?\" is marked as an h4, which may not follow a semantically correct order of headings. To fix this, ensure that heading levels only increase by one. For example, if the preceding heading is an h2, the \"What is GNU?\" heading should be an h3.\n\n```html\n<h3>What is GNU?</h3>\n```\n\n2. **Contrast Ratio Violation** (ContrastAgent): The contrast ratio of the text within the li elements is below the recommended minimum. To fix this, adjust the foreground and/or background colors to meet the WCAG recommended minimum contrast ratio of 4.5:1 for normal text.\n\n```css\nli {\n    color: #FFFFFF; /* Adjusted foreground color */\n    background-color: #A32D2A; /* Adjusted background color */\n}\n```\n\n3. **Landmark Violations** (AxeViolationsAgent): The page lacks unique landmarks and some content is not contained by landmarks. To fix this, ensure all content is contained by landmarks and that each landmark is unique.\n\n```html\n<!-- Example of a unique landmark -->\n<main aria-labelledby=\"mainHeading\">\n    <h1 id=\"mainHeading\">Main Content</h1>\n    <!-- Main content goes here -->\n</main>\n```\n\n4. **Missing Level-One Heading** (AxeViolationsAgent): The page lacks a level-one heading. To fix this, include a level-one heading that describes the main content of the page.\n\n```html\n<h1>Main Content of the Page</h1>\n```\n\n5. **Image Alternative Text** (ImageCaptioningAgent): Some of the generated captions do not accurately describe the images based on their alternative text. To fix this, ensure that the alternative text accurately describes the content of the image.\n\n```html\n<!-- Example of an image with accurate alternative text -->\n<img src=\"image.jpg\" alt=\"Accurate description of the image\">\n```",
        "name": "FixingAgent",
        "role": "user"
    }
]
}


IMAGE_PATH_MAP = {
    "Google": "webp\google.webp",
    "Microsoft": "webp\microsoft.webp",
    "GNU": "webp\gnu.webp"
}

# ----------------------
# UI: Website Selection
# ----------------------
st.selected_site = st.selectbox("Select a website for analysis", list(SITE_JSON_MAP.keys()))
DUMMY_RESPONSE = SITE_JSON_MAP[st.selected_site]

# ----------------------
# Parse FixingAgent Suggestions
# ----------------------
fix_item = next(item for item in DUMMY_RESPONSE if item['name'] == 'FixingAgent')
content = fix_item['content']
raw_sugs = re.split(r'\n\n(?=\d+\.)', content)
sugs = raw_sugs[1:]

# ----------------------
# Initialize Feedback
# ----------------------
if 'feedback' not in st.session_state:
    st.session_state.feedback = []

# ----------------------
# App Title
# ----------------------
st.markdown("# Accessibility Agent Lab")

# ----------------------
# Tabs: Review & Stats
# ----------------------
tab1, tab2 = st.tabs(["Review", "Stats"])

# ----------------------
# Review Tab: Display Detections & Fixes
# ----------------------
with tab1:
    st.header("🔍 Detection Agent Findings")
    title_map = {
        'semantic-agent': 'Semantic',
        'contrast-agent': 'Contrast',
        'axe-violations-agent': 'Axe Violations',
        'image-captioning-agent': 'Image Captioning',
        'VisuallyImpairedAgent': 'Visually Impaired',
        'MotorImpairedAgent': 'Motor Impaired',
        'ColorBlindAgent': 'Color Blind',
    }
    detections = [d for d in DUMMY_RESPONSE if d['name'] in title_map]
    for key, title in title_map.items():
        st.subheader(f"{title} Agent Findings")
        entries = [d['content'] for d in detections if d['name'] == key]
        if not entries:
            st.success("No issues detected ✓")
        for e in entries:
            st.info(e)

    st.markdown("---")

    img_path = IMAGE_PATH_MAP.get(st.selected_site)
    if img_path and Path(img_path).exists():
        st.image(img_path, caption=f"Screenshot: {st.selected_site}")
    else:
        st.warning(f"Screenshot not found for {st.selected_site} at {img_path}")

    st.markdown("---")

    st.header("🛠️ Fixing Agent Suggestions for " + st.selected_site)
    for idx, suggestion in enumerate(sugs, start=1):
        st.subheader(f"Suggestion {idx}")
        st.markdown(suggestion, unsafe_allow_html=True)
        col_up, col_down = st.columns(2)
        if col_up.button("👍 Upvote", key=f"up_{st.selected_site}_{idx}"):
            st.session_state.feedback.append({'site': st.selected_site, 'fix_index': idx, 'action': 'up'})
            col_up.success("Upvoted")
        if col_down.button("👎 Downvote", key=f"down_{st.selected_site}_{idx}"):
            st.session_state.feedback.append({'site': st.selected_site, 'fix_index': idx, 'action': 'down'})
            col_down.error("Downvoted")

# ----------------------
# Stats Tab: Aggregate Feedback
# ----------------------
with tab2:
    st.header(f"📊 Feedback Stats for {st.selected_site}")
    df = pd.DataFrame(st.session_state.feedback)
    if df.empty:
        st.info("No feedback yet – vote on suggestions in the Review tab.")
    else:
        # Filter by selected site
        df_site = df[df.site == st.selected_site]
        if df_site.empty:
            st.info(f"No feedback yet for {st.selected_site}.")
        else:
            # Group by site & fix_index
            summary = df_site.groupby(['site', 'fix_index']).action \
                .value_counts().unstack(fill_value=0).reset_index()
            summary['total'] = summary.get('up', 0) + summary.get('down', 0)
            summary['agreement'] = summary.get('up', 0) / summary['total']
            summary = summary.rename(columns={'up': 'Upvotes', 'down': 'Downvotes'})

            st.subheader("Per-Suggestion Summary")
            st.dataframe(summary[['site', 'fix_index', 'Upvotes', 'Downvotes']])

            total_votes = int(df_site.shape[0])
            up_votes = int(df_site['action'].value_counts().get('up', 0))
            down_votes = int(df_site['action'].value_counts().get('down', 0))
            agreement = up_votes / total_votes if total_votes else 0

            st.subheader("Overall Metrics")
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Total Votes", total_votes)
            c2.metric("👍 Upvotes", up_votes)
            c3.metric("👎 Downvotes", down_votes)
            c4.metric("Agreement", f"{agreement:.0%}")
