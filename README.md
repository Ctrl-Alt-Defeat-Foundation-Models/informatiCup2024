## Usage

### Prerequisites

```bash
pip install -e .
```

### How to run the command line

You can see all the possible command using the command 
```bash
fad --help
```
General commands are: `fad generate ...`, `fad process ...`, `fad evaluate ...`

Types of generators: `fake_generator_text`, `fake_generator_image`
Types of processors: `naive_processor_text`, `naive_processor_image`
Types of evaluators: `roberta_evaluator_text`, `umm_maybe_evaluator_image`

A possible pipeline command for a text would be:
```bash
fad pipeline fake_generator_text naive_processor_text roberta_evaluator_text
```

and for an image:
```bash
fad pipeline fake_generator_image naive_processor_image umm_maybe_evaluator_image
```
