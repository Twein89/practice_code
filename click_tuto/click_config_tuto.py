import click
from pprint import pprint
import six


def read_config(ctx, param, value):
    if not value:
        return {}
    import json

    def underline_dict(d):
        if not isinstance(d, dict):
            return d
        return dict((k.replace('-', '_'), underline_dict(v)) for k, v in six.iteritems(d))

    config = underline_dict(json.load(value))
    ctx.default_map = config
    return config


@click.group(invoke_without_command=True)
@click.option('-c', '--config', callback=read_config, type=click.File('r'))
@click.pass_context
def cli(ctx, **kwargs):
    print(ctx.obj)
    pprint(kwargs)
    return kwargs

class ObjectDict(dict):
    """
    Object like dict, every dict[key] can visite by dict.key

    If dict[key] is `Get`, calculate it's value.
    """
    def __getattr__(self, name):
        ret = self.__getitem__(name)
        if hasattr(ret, '__get__'):
            return ret.__get__(self, ObjectDict)
        return ret


if __name__ == '__main__':
    cli()

    # print()


