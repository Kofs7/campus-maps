load("@python_deps//:requirements.bzl", "requirement")

py_binary(
    name = "geolocater",
    srcs = ["geolocater.py"],
    data = [":locations.json"],
    deps = [requirement("mapbox")],
)
