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

The supported input arguments are:

|Argument|Description|
|---|---|
|snap_name|Name of the snap being built (i.e. `edgexfoundry`/`edgex-device-camera`)|
|architecture|Target build architecture, such as: `amd64`, `arm64`, `armhf`|
|consumer_name|Launchpad consumer name (aka. consumer key)|
|access_token|Launchpad access token|
|access_secret|Launchpad access secret|

The three secrets used to connect to Launchpad, `consumer_name`, `access_token` and `access_secret` should be generated and stored as Github Secrets.

To regenerate the secrets, if needed, do the following:
- copy this [Python script](https://github.com/canonical/edgex-sync/blob/main/utils/create-lp-credentals.py) to your computer.
- run the script locally
- It will prompt you to log into launchpad
- A `credentials` file will be generated with the secrets. Use the contents of that file (consumer_key, access_token, access_secret) to create the Github secrets.

Note that to generate the credentials you need to be member of a Launchpad team with full access to the snap recipes, such as the [Canonical EdgeX Team](https://launchpad.net/~canonical-edgex)
