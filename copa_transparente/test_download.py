# coding: utf-8
import io
import sys
import urllib.request as request
from unittest import mock, TestCase

BUFF_SIZE = 1024

def download_length(response, output, length):
    times = length // BUFF_SIZE
    if length % BUFF_SIZE > 0:
        times += 1
    for time in range(times):
        output.write(response.read(BUFF_SIZE))
        print("Downloaded %d" % (((time * BUFF_SIZE)/length)*100))

class DownloadTest(TestCase):

    def test_download_whit_know_length(self):
        response = mock.MagicMock()
        response.read = mock.MagicMock(side_efect=['Data']*2)

        output = mock.MagicMock()
        download_length(response, output, 1024)

        calls = [mock.call(BUFF_SIZE)]
        response.read.assert_has_calls(calls)

        calls = [mock.call('Data'), mock.call('Data')]
