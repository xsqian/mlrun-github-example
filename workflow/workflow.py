""" The main workflow of the project

This file creates the MLRun pipeline to run the functions
in an orchestrated manner

"""

from kfp import dsl
import mlrun

# Create a Kubeflow Pipelines pipeline
@dsl.pipeline(name="testing-resource")
def test():
    project = mlrun.get_current_project()
    func = project.get_function("nodegroup-test")
    func.with_requests(mem="16G", cpu=2)
    func.with_limits(mem="32G", cpu=4)    
    run2 = mlrun.run_function(
        name="nodegroup-test-run-from-workflow",
        function=func,
        auto_build=False,
        local=False,
    )
