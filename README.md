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
Types of evaluators: `roberta_evaluator_text`

A possible pipeline command would be:
```bash
fad pipeline fake_generator_text naive_processor_text roberta_evaluator_text
```
