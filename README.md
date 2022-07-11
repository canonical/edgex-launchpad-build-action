# edgex-launchpad-build-action

This is a Github Action which is used by the [edgex-sync GitHub Workflows](https://github.com/canonical/edgex-sync).

It is used to request a build of an EdgeX snap on Launchpad.

Example of using this action in a workflow:

```
  build-launchpad:
    runs-on: ubuntu-latest
    needs: test-snap
    steps:
      - name: Kick off Launchpad build
        uses: canonical/edgex-launchpad-build-action@v1.4
        with:
          snap_name: "edgexfoundry"
          architecture: amd64
          consumer_name: ${{ secrets.LP_CONSUMER_NAME }}
          access_token: ${{ secrets.LP_ACCESS_TOKEN }}
          access_secret: ${{ secrets.LP_ACCESS_SECRET }}
```

Refer to [`action.yml`](action.yml) to find the list of supported input arguments.

## Secrets
The three secrets used to connect to Launchpad, `consumer_name`, `access_token` and `access_secret` should be generated and stored as Github Secrets.

To regenerate the secrets, do the following:
- Run [`create-lp-credentals.py`](create-lp-credentals.py) Python script locally.
- It will prompt you to log into Launchpad
- A `credentials` file will be generated with the secrets. Use the contents of that file (consumer_key, access_token, access_secret) to create the Github secrets. Consumer key should be used as the consumer name.

Note that to generate the credentials you need to be member of a Launchpad team with full access to the snap recipes, such as the [Canonical EdgeX Team](https://launchpad.net/~canonical-edgex)

## Run locally
```
CONSUMER_NAME="" ACCESS_TOKEN="" ACCESS_SECRET="" SNAP_NAME="" ARCH=amd64 UBUNTU_SERIES=focal python request-build.py
```
