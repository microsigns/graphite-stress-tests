graphite-stress-tests
=====================

This repository is a mix of playground for stress test scenarios for graphite
and finished tests ready to be run

metricfactory
-------------

[Wishbone][wishbone] is a framework to easily build event-driven servers. It
allows describing event pipelines from yaml files. It has it's own internal
metrics format, and a module that knows how to convert them to graphite format

"[Metricfactory][metricfactory] is a set of [wishbone][wishbone] modules to
build metric processing servers". In particular, it has a module called hammer
that just makes up random metrics with some predefined details (the metrics
names) as fast as it can.

In the metricfactory/sandbox directory you can find the metricfactory graphite
examples, and their history (might need a --follow parameter passed to git log
because there was some file renaming)

In the metricfactory/tests directory you can find the selected test scenarios
ready to be run against the graphite servers. To run them, change the
modules.tcp.arguments.host value to the desired graphite server and adjust the
port accordingly.

I've added to the wishbone graphite module the hability to send pickled metrics
to graphite. For this to work, it needs to receive a list of metrics instead
of a single one. It will pack them and send them together. For this the
"tippingbucket" module is used. The tippingbucket module accumulates events
(metrics, in this case) until a certain number is reached, or certain time goes
by, See metricfactory/sandbox/hammer_scenario_pickle.yaml for an example.

To run these tests, install the requirements by running

```
pip install -r metricfactory/requirements.txt
```

and then run e.g.:

```
metricfactory debug --config metricfactory/tests/100_100_infinite_pickle.yaml
```

The only necessary tweaking should be changing the graphite server's ip address

To run multiple (8 in this example) instances in parallel (different processes)
run

```
metricfactory debug --instances 8 --config metricfactory/tests/100_100_infinite_pickle.yaml
```

[metricfactory]: https://github.com/smetj/metricfactory
[wishbone]: https://wishbone.readthedocs.org/en/latest/
