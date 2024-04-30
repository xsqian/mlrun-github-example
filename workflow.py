
from kfp import dsl
import mlrun

# Create a Kubeflow Pipelines pipeline
@dsl.pipeline(
    name="Coffee Rating Pipeline"
)
def pipeline():
    
    # Run the data creationg function
    ingest = mlrun.run_function(
        "coffeerating_data_function",
        name="coffee-data-generation-step",
        outputs=['coffee_dataset'],
        local=False,
    )

    # Train a model using the trainer function
    train = mlrun.run_function(
        "coffeerating-trainer",
        inputs={"dataset": ingest.outputs['coffee_dataset']},
        outputs=["model"],
        local=False
    )
