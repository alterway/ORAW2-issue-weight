# ORAW2_Issue-weight

This repository features a regressor capable to predict the priority of french issue reports by giving it a weight.

This service was created as a result of the OpenReq project funded by the European Union Horizon 2020 Research and Innovation programme under grant agreement No 732463.

## usage

\[WIP]

The swagger api definition can be found [here](TODO).

The API consist of single endpoint `/issue_weighting` taking a json payload with the keys:

- Title string
- Body string

and returning an object with the keys:

- weight integer, the higher is the most urgent
- stance integer, the higher is the more positive

## Technologies

The regressor is coded for python 3.5+, we recommand running this project via docker.

The regressor is based on [scikit-learn](scikit-learn.org) and the user stance if provided by [SentiStrength](http://sentistrength.wlv.ac.uk).

## Build & Run

[SentiStrength](http://sentistrength.wlv.ac.uk) Java is required to build the image, the jar file must be placed at the root of the project. To acquire SentiStrength please refer to SentiStrength website.

```bash
docker build . --rm -t issue_weighting:1
docker run --rm -p 8080:8080 --name issue_weighting -it issue_weighting:1 oraw1
```

## License

Free use of this software is granted under the terms of the EPL version 2 (EPL2.0).