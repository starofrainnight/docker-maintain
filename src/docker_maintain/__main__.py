import sys
import docker
import json
import argparse
import six

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
                six.print_(line)

def clean(args):
    client = docker.Client(base_url=args.base_url)
    images = client.images()
    for image in images:
        is_need_remove = True
        if image["RepoTags"] is not None:
            for repo_tag in image["RepoTags"]:
                if "<none>" not in repo_tag:
                    # Images that don't have "<none>" should be ignored
                    is_need_remove = False
                    break

        if not is_need_remove:
            continue

        image_id = image["Id"]
        six.print_("Removing image : %s ..." % image)
        try:
            client.remove_image(image_id, force=args.force)
        except docker.errors.APIError as e:
            six.print_("ERROR! %s" % e.explanation.decode("utf-8"))

def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    description = "Docker maintain commands"
    parser = argparse.ArgumentParser(description=description)
    subparsers = parser.add_subparsers(dest='cmd', help='sub-commands')
    subparsers.required = True

    subpraser = subparsers.add_parser(
        'pull-all', help='Pull all images with correct repository name and tags')
    subpraser.set_defaults(func=pull_all)
    subpraser.add_argument('--base_url', default=None)

    subpraser = subparsers.add_parser(
        'clean', help='Clean all images with "<none>"')
    subpraser.set_defaults(func=clean)
    subpraser.add_argument('--base_url', default=None)
    subpraser.add_argument('--force', action='store_true')

    args = parser.parse_args(args)
    return args.func(args)

if __name__ == "__main__":
    main()
