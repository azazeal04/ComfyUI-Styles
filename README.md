# ComfyUI Styler, a custom node for ComfyUI

ComfyUI Styler is a node that enables you to style prompts based on predefined templates stored in multiple JSON files. The node specifically replaces a {prompt} placeholder in the 'prompt' field of each template with provided positive text.

The node also effectively manages negative prompts. If negative text is provided, the node combines this with the 'negative_prompt' field from the template. If no negative text is supplied, the system defaults to using the 'negative_prompt' from the JSON template. This flexibility enables the creation of a diverse and specific range of negative prompts.

## Changelog
This section details the updates and new features committed over time, organized chronologically with the most recent changes at the top.

### Commit date (2023-10-10)

#### New Features

* **ComfyUI Styler Advanced**: New node for more elaborate workflows with lingustic and supportive terms. Selector to change the split behavior of the negative prompt. Special thanks to @WinstonWoof and @Danamir for their contributions!
* **ComfyUI Styler**: Minor changes to output names and printed log prompt.


#### New Features

* **Loading from Multiple JSON Files:** The system can now load styles from multiple JSON files present in the specified directory, ensuring the uniqueness of style names by appending a suffix to duplicates.
* **Enhanced Error Handling:** Improved error handling for file reading, data validity, and template replacement functions.


```

### Installation

To install and use the ComfyUI Styler nodes, follow these steps:

1. Open a terminal or command line interface.
2. Navigate to the `ComfyUI/custom_nodes/` directory.
3. Run the following command:
```git clone https://github.com/azazeal04/ComfyUI-Styles.git```
4. Restart ComfyUI.

This command clones the ComfyUI Styler repository into your `ComfyUI/custom_nodes/` directory. You should now be able to access and use the nodes from this repository.

### Inputs

* **text_positive** - text for the positive base prompt
* **text_negative** - text for the negative base prompt
* **log_prompt** - print inputs and outputs to stdout

### Outputs

* **text_positive** - combined prompt with style for positive promt
* **text_negative** - combined prompt with style for negative promt
