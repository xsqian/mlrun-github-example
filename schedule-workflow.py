
from kfp import dsl
import mlrun


# Create a Kubeflow Pipelines pipeline
@dsl.pipeline(
    name="scheduled-pipeline",
    description="Example of scheduled pipeline"
)
def pipeline():
    
    # Get current project
    project = mlrun.get_current_project()

    f1 = project.get_function("function1")

    # Ingest the data set
    f1_rs = project.run_function(
        function=f1
    )

    project.run_function(
        function=f1
    ).after(f1_rs)
