import sys
import docker
import json
import argparse

def pull_all(args):
    client = docker.Client(base_url=args.base_url)
    images = client.images()
    for image in images:
        if image["RepoTags"] is None:
            # Ignored images that does not have repository or tags
            continue

        for repo_tag in image["RepoTags"]:
            if "<none>" in repo_tag:
                # Ignored images that have "<none>"
                continue

            splitted = repo_tag.split(":")
            repo = splitted[0]
            tag = splitted[1]

            for line in client.pull(repository=repo, tag=tag, stream=True):
                print(line)

def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    description = "Docker maintain commands"
    parser = argparse.ArgumentParser(description=description)
    subparsers = parser.add_subparsers(help='sub-commands')

    parser_pull_all = subparsers.add_parser(
        'pull-all', help='Pull all images with correct repository name and tags')
    parser_pull_all.set_defaults(func=pull_all)
    parser_pull_all.add_argument('--base_url', default=None)

    args = parser.parse_args(args)
    return args.func(args)

if __name__ == "__main__":
    main()
