## Usage

### Prerequisites

```shell
pip install -e .
```

### How to run the command line

You can see all the possible command using the command 
```shell
fad --help
```
General commands are: `fad generate ...`, `fad process ...`, `fad evaluate ...`, `fad command-list ...`

The basic processing command is: 
```shell
fad process INPUT_FILE_PATH OUTPUT_FILE_PATH --processor PROCESSOR_NAME [OPTIONAL]
```

So a simple example would be:
```shell
fad process fool_ai_detector/resources/ai_gen_images/berries.jpg fool_ai_detector/resources/ai_gen_images/processed_berries.png
```

Types of models for the different tasks(generate/process/evaluate) can be listed with: 
```shell
fad command-list TASK BOOL_IMAGE
```

E. g. the command to list all possible image generators would be:
```shell
fad command-list generate 1
```


We used the pipeline command to test our different processors.

A possible pipeline command for a text would be:
```shell
fad pipeline fake_generator_text naive_processor_text roberta_evaluator_text
```

and for an image:
```shell
fad pipeline fake_generator_image naive_processor_image umm_maybe_evaluator_image
```
