[![.github/workflows/demo.yaml](https://github.com/effigies/hatchling-namespace-demo/actions/workflows/demo.yaml/badge.svg)](https://github.com/effigies/hatchling-namespace-demo/actions/workflows/demo.yaml)

# Namespace packaging demo

This repository demonstrates using [hatchling][] and [hatch-vcs][] to generate namespace
packages that reside within a submodule of a base package.

The logical module is:

```
myproj  # Provided by myproj package
  myproj.submod1
  myproj.tasks
    myproj.tasks.task1  # Provided by myproj-task1 package
    myproj.tasks.task2  # Provided by myproj-task2 package
```

This repository demonstrates that these can be provided by independent packages. It does
this in a [monorepo][], also demonstrating the using multiple `pyproject.toml`-defined
packages within a single repository.

See the [CI results](https://github.com/effigies/hatchling-namespace-demo/actions/workflows/demo.yaml)
to verify the functionality.

[hatchling]: https://hatch.pypa.io/
[hatch-vcs]: https://github.com/ofek/hatch-vcs
[monorepo]: https://en.wikipedia.org/wiki/Monorepo
