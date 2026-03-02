# CI/CD

poreFlow uses Continuous Integration/Continuous Deployment (CI/CD) to automate 
package testing, building, and packaging.

## Prerequisites
- Docker. Which can be downloaded and installed [here][Docker Install].

## Create and configure the GitLab runners

The easiest way to set up the runners is using [Docker Compose]. Create the folder with the following files:
```
gitlab-runner
 ├─  config
 │     └─ config.toml
 └─  compose.yaml
```

`compose.yaml` contains the instructions for Docker and `config.toml` specifies the configuration of the GitLab 
runners. The GitLab runner needs an authentication token, which can be created when 
[registering a GitLab runner][GitLab Runner Register]. `config.toml` should look like:

```toml title="config.toml" linenums="1"
log_level = "warning"

[[runners]]
  name = "gitlab-runner-1"
  url = "https://gitlab.tudelft.nl"
  executor = "docker"
  token = "paste-your-token-here"
  limit = 0
  [runners.docker]
    tls_verify = false
    image = "docker:latest"
    privileged = true
    disable_cache = false
    pull_policy = "if-not-present"
    helper_image = "registry.gitlab.com/gitlab-org/gitlab-runner/gitlab-runner-helper:alpine-edge-arm-1fd8d947"
    volumes = ["/var/run/docker.sock:/var/run/docker.sock", "/cache"]
  [runners.cache]
    Insecure = false
```

`compose.yaml` should look like:

```yaml title="compose.yml" linenums="1"
services:
  gitlab-runner:
    image: docker.io/gitlab/gitlab-runner:alpine3.21-bleeding
    container_name: gitlab-runner-1
    volumes:
      - ./config/config.toml:/etc/gitlab-runner/config.toml:ro
      - /var/run/docker.sock:/var/run/docker.sock
    restart: unless-stopped
```


To start the runners, open a terminal in the folder containng `compose.yaml` and run:
```shell linenums="1"
docker compose up -d
```


## Troubleshooting

During the project, at some point we had Docker runners both on a MacOS M3 machine and an Intel machine. 
The former builds for the platform `linux_aarch64` while the latter built for `manylinux_2_41_x86_64`. 
`.gitlab-ci.yml` does not take this into account so builds from one machine would not install for testing 
on another machine. In this case, ensure that only one machine hosting the runners is on at any given time.



[Docker Install]: https://docs.docker.com/get-started/get-docker/
[Docker Compose]: https://docs.docker.com/compose/
[GitLab Runner Register]: https://docs.gitlab.com/runner/register/