#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

task_config = {}


task_config['frontend_version'] = 1

"""A short and descriptive title about the kind of task the HIT contains.
On the Amazon Mechanical Turk web site, the HIT title appears in search results,
and everywhere the HIT is mentioned.
"""
task_config['hit_title'] = 'Caption an image in a specified word count'


"""A description includes detailed information about the kind of task the HIT contains.
On the Amazon Mechanical Turk web site, the HIT description appears in the expanded
view of search results, and in the HIT and assignment screens.
"""
task_config['hit_description'] = (
    'Provide a caption to an image, you will be given a word range to use. '
    'Ensure your caption fits in the provided window.'
)

"""One or more words or phrases that describe the HIT, separated by commas.
On MTurk website, these words are used in searches to find HITs.
"""
task_config['hit_keywords'] = 'image captioning,vision'


"""A detailed task description that will be shown on the HIT task preview page
and on the left side of the chat page. Supports HTML formatting.
"""
task_config['task_description'] = (
    'Provide a caption to an image, you will be given a word range to use. '
    'Ensure your caption fits in the provided window.'
)
