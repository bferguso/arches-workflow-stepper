import re
from django_hosts import patterns, host

host_patterns = patterns(
    "",
    host(
        re.sub(r"_", r"-", r"arches_workflow_stepper"),
        "arches_workflow_stepper.urls",
        name="arches_workflow_stepper",
    ),
)
