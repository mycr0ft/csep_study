import graphviz
from jinja2 import Template, Environment, FileSystemLoader

inputs = """Life cycle concepts
Operational System
Maintained and Sustained System
Trained Personnel
Operation Report
Maintenance and Logistics Report""".split("\n")

activities = [ "Prepare for Disposal",
               "Perform Disposal",
               "Finalize the Disposal" ]

outputs =  """Disposal Strategy/Approach
Disposal Procedure
Disposed System
Constraints on Solution
Requirements Imposed on Enabling Systems
Traceability Mapping
Disposal Report
Disposal Records/Artifacts""".split("\n")



env = Environment( loader = FileSystemLoader('templates'))
template = env.get_template( 'ioblock.jinja')

inputs_label = template.render( title = "Inputs", inputs=inputs)
#print(inputs_label)

activities_label = template.render( title = 'Activities', inputs=activities)
outputs_label = template.render( title = 'Outputs', inputs=outputs)

diagram = graphviz.Digraph('test ipo', engine='dot')

diagram.node( 'inputs', label=inputs_label, shape="plain")
diagram.node( 'activities', label=activities_label, shape="plain")
diagram.node( 'outputs', label=outputs_label, shape="plain")
diagram.node( 'controls', label="Controls", shape="rect")
diagram.node( 'enablers', label="Enablers", shape="rect")
diagram.edge( 'inputs', 'activities', dir="both", arrowtail="none", arrowhead="vee") 
diagram.edge( 'activities', 'outputs', dir="both", arrowtail="none", arrowhead="vee") 
diagram.edge( 'controls', 'activities', dir="both", arrowtail="none", arrowhead="vee") 
diagram.edge( 'enablers', 'activities', dir="both", arrowtail="none", arrowhead="vee") 
diagram.format = 'svg'
diagram.render( 'ipo-diag-disposal')


